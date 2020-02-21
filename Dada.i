%module cDada

%{
#define SWIG_FILE_WITH_INIT
#include "DadaHeader.h"
#include "SortedDada.h"
using namespace dada;
%}

%include "exception.i"
%include "numpy.i"
%init %{
    import_array();
%}

%typemap(out) std::vector<float>& {
        npy_intp length = ($1)->size();
        $result = PyArray_SimpleNewFromData(1, &length, NPY_FLOAT32, ($1)->data());
}

%typemap(out) std::vector<char>& {
        npy_intp length = ($1)->size();
        $result = PyArray_SimpleNewFromData(1, &length, NPY_INT8, ($1)->data());
}

%typemap(out) std::vector<std::complex<float> >& {
        npy_intp length = ($1)->size();
        $result = PyArray_SimpleNewFromData(1, &length, NPY_COMPLEX64, ($1)->data());
}

%typemap(in) std::vector<std::complex<float> >& (std::vector<std::complex<float> > temp) {
    if (!PyArray_Check($input)) {
        SWIG_exception(SWIG_TypeError, "NumPy array expected");
    }
    PyArrayObject *arr = (PyArrayObject*)$input;
    if ( PyArray_TYPE(arr) != NPY_COMPLEX64 ) {
        SWIG_exception(SWIG_TypeError, "Array type should be 'Complex64'");
    }
    PyArrayObject *arr1d = (PyArrayObject *)PyArray_Ravel(arr, NPY_CORDER);
    const std::size_t size = PyArray_DIM(arr1d, 0);
    temp.resize(size);
    std::complex<float> *arr_data = static_cast<std::complex<float>*>(PyArray_DATA(arr1d));
    if (PyArray_ISCONTIGUOUS(arr1d)) {
        std::copy(arr_data, arr_data + size, temp.begin());
    } else {
        const npy_intp strides = PyArray_STRIDE(arr1d, 0)/sizeof(std::complex<float>);
        for (std::size_t i = 0; i < size; i++)
            temp[i] = arr_data[i*strides];
    }
    $1 = &temp;
}

%typemap(in) std::vector<char>& (std::vector<char> temp) {
    if (!PyArray_Check($input)) {
        SWIG_exception(SWIG_TypeError, "NumPy array expected");
    }
    PyArrayObject *arr = (PyArrayObject*)$input;
    if ( PyArray_TYPE(arr) != NPY_INT8 ) {
        SWIG_exception(SWIG_TypeError, "Array type should be 'int8'");
    }
    PyArrayObject *arr1d = (PyArrayObject *)PyArray_Ravel(arr, NPY_CORDER);
    const std::size_t size = PyArray_DIM(arr1d, 0);
    temp.resize(size);
    char *arr_data = static_cast<char*>(PyArray_DATA(arr1d));
    if (PyArray_ISCONTIGUOUS(arr1d)) {
        std::copy(arr_data, arr_data + size, temp.begin());
    } else {
        const npy_intp strides = PyArray_STRIDE(arr1d, 0)/sizeof(char);
        for (std::size_t i = 0; i < size; i++)
            temp[i] = arr_data[i*strides];
    }
    $1 = &temp;
}

%include "DadaHeader.h"
%include "SortedDada.h"
