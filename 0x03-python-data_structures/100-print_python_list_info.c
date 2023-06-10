#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);
	PyListObject *obj = (PyListObject *)p;
	PyObject **items = obj->ob_item;

	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (int i = 0; i < size; i++)
		printf("Element %i: %s\n", i, Py_TYPE(items[i])->tp_name);
}
