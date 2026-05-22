#include <Python.h>
#include <string.h>
#include <stdlib.h>

void dbc2dbf(char** input_file, char** output_file);

static PyObject *
pyreaddbc_dbc2dbf(PyObject *self, PyObject *args)
{
    char *input_file, *output_file;

    if (!PyArg_ParseTuple(args, "ss", &input_file, &output_file))
        return NULL;

    dbc2dbf(&input_file, &output_file);

    Py_RETURN_NONE;
}

static PyMethodDef PyreaddbcMethods[] = {
    {"dbc2dbf", pyreaddbc_dbc2dbf, METH_VARARGS,
     "Decompress a .dbc file to a .dbf file."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef pyreaddbcmodule = {
    PyModuleDef_HEAD_INIT,
    "_readdbcmodule",
    NULL,
    -1,
    PyreaddbcMethods
};

PyMODINIT_FUNC
PyInit__readdbcmodule(void)
{
    return PyModule_Create(&pyreaddbcmodule);
}
