#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	int size = PyList.Size(p);

	printf("[*] Size of the Python List = %d", size);
	printf("[*] Allocated = %d", Py_SIZE(p));
	for (int i = 0; i < size; i++)
	{
		printf("Element %d: %s", i, Py_TYPE(PyList_GetItem(p, 1)))
	}

}
