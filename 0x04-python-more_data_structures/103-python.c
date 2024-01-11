#include <Python.h>

/**
 * print_python_bytes - prints info about Python bytes objects
 * @p: PyObject pointer
 */
void print_python_bytes(PyObject *p)
{
    printf("[.] bytes object info\n");
    if (PyBytes_Check(p))
    {
        Py_ssize_t size = PyBytes_Size(p);
        char *string = PyBytes_AsString(p);

        printf("  size: %ld\n", size);
        printf("  trying string: %s\n", string);
        printf("  first 10 bytes: ");
        for (Py_ssize_t i = 0; i < size && i < 10; ++i)
            printf("%02x ", string[i] & 0xFF);
        printf("\n");
    }
    else
    {
        printf("  [ERROR] Invalid Bytes Object\n");
    }
}

/**
 * print_python_list - prints info about Python lists
 * @p: PyObject pointer
 */
void print_python_list(PyObject *p)
{
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (Py_ssize_t i = 0; i < PyList_Size(p); ++i)
    {
        PyObject *element = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);

        if (PyBytes_Check(element))
            print_python_bytes(element);
    }
}
