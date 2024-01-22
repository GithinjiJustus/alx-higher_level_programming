#include <stdio.h>
#include <Python.h>

/**
 * print_python_float - Prints information about a PyFloatObject
 * @p: Pointer to a PyObject
 */
void print_python_float(PyObject *p)
{
    double value = 0;
    char *string = NULL;

    fflush(stdout);
    printf("[.] float object info\n");

    // Check if the object is a PyFloatObject
    if (!PyFloat_CheckExact(p))
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    // Extract the value from the PyFloatObject
    value = ((PyFloatObject *)p)->ob_fval;

    // Convert the float value to a string
    string = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);

    // Print the information
    printf("  value: %s\n", string);
}

/**
 * print_python_bytes - Prints information about a PyBytesObject
 * @p: Pointer to a PyObject
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t size = 0, i = 0;
    char *string = NULL;

    fflush(stdout);
    printf("[.] bytes object info\n");

    // Check if the object is a PyBytesObject
    if (!PyBytes_CheckExact(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    // Extract size and string from the PyBytesObject
    size = PyBytes_Size(p);
    string = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));

    // Print size and string information
    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", string);
    printf("  first %zd bytes:", size < 10 ? size + 1 : 10);

    // Print the first 10 bytes of the string
    while (i < size + 1 && i < 10)
    {
        printf(" %02hhx", string[i]);
        i++;
    }

    printf("\n");
}

/**
 * print_python_list - Prints information about a PyListObject
 * @p: Pointer to a PyObject
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t size = 0;
    PyObject *item;
    int i = 0;

    fflush(stdout);
    printf("[*] Python list info\n");

    // Check if the object is a PyListObject
    if (PyList_CheckExact(p))
    {
        // Extract size and allocated space information
        size = PyList_GET_SIZE(p);
        printf("[*] Size of the Python List = %zd\n", size);
        printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

        // Iterate over the elements of the list
        while (i < size)
        {
            // Extract the current item
            item = PyList_GET_ITEM(p, i);

            // Print element information
            printf("Element %d: %s\n", i, item->ob_type->tp_name);

            // Check if the item is a PyBytesObject and print its information
            if (PyBytes_Check(item))
                print_python_bytes(item);
            // Check if the item is a PyFloatObject and print its information
            else if (PyFloat_Check(item))
                print_python_float(item);

            i++;
        }
    }
    else
    {
        printf("  [ERROR] Invalid List Object\n");
    }
}
