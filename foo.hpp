#define PY_MAJOR_VERSION 3
#undef ENABLE_PYTHON_MODULE
#include <pythonic/core.hpp>
#include <pythonic/python/core.hpp>
#include <pythonic/types/bool.hpp>
#include <pythonic/types/int.hpp>
#ifdef _OPENMP
#include <omp.h>
#endif
#include <pythonic/include/builtins/print.hpp>
#include <pythonic/include/types/str.hpp>
#include <pythonic/builtins/print.hpp>
#include <pythonic/types/str.hpp>
namespace 
{
  namespace __pythran_foo
  {
    struct foo
    {
      typedef void callable;
      ;
      struct type
      {
        typedef pythonic::types::str __type0;
        typedef typename pythonic::returnable<__type0>::type __type1;
        typedef __type1 result_type;
      }  ;
      inline
      typename type::result_type operator()() const;
      ;
    }  ;
    struct a
    {
      typedef void callable;
      typedef void pure;
      struct type
      {
        typedef pythonic::types::str __type0;
        typedef typename pythonic::returnable<__type0>::type __type1;
        typedef __type1 result_type;
      }  ;
      inline
      typename type::result_type operator()() const;
      ;
    }  ;
    inline
    typename foo::type::result_type foo::operator()() const
    {
      pythonic::builtins::functor::print{}(pythonic::types::str("This is change to c++ test"));
      return pythonic::types::str("This is change to c++ test");
    }
    inline
    typename a::type::result_type a::operator()() const
    {
      {
        static typename a::type::result_type tmp_global = pythonic::types::str("This is change to c++ test");
        return tmp_global;
      }
    }
  }
}
#include <pythonic/python/exception_handler.hpp>
#ifdef ENABLE_PYTHON_MODULE
static PyObject* a = to_python(__pythran_foo::a()());
inline
typename __pythran_foo::foo::type::result_type foo0() 
{
  
                            PyThreadState *_save = PyEval_SaveThread();
                            try {
                                auto res = __pythran_foo::foo()();
                                PyEval_RestoreThread(_save);
                                return res;
                            }
                            catch(...) {
                                PyEval_RestoreThread(_save);
                                throw;
                            }
                            ;
}

static PyObject *
__pythran_wrap_foo0(PyObject *self, PyObject *args, PyObject *kw)
{
    PyObject* args_obj[0+1];
    (void)args_obj;
    char const* keywords[] = { nullptr};
    if(! PyArg_ParseTupleAndKeywords(args, kw, "",
                                     (char**)keywords ))
        return nullptr;
    if(1)
        return to_python(foo0());
    else {
        return nullptr;
    }
}

            static PyObject *
            __pythran_wrapall_foo(PyObject *self, PyObject *args, PyObject *kw)
            {
                return pythonic::handle_python_exception([self, args, kw]()
                -> PyObject* {

if(PyObject* obj = __pythran_wrap_foo0(self, args, kw))
    return obj;
PyErr_Clear();

                return pythonic::python::raise_invalid_argument(
                               "foo", "\n""    - foo()", args, kw);
                });
            }


static PyMethodDef Methods[] = {
    {
    "foo",
    (PyCFunction)__pythran_wrapall_foo,
    METH_VARARGS | METH_KEYWORDS,
    "Supported prototypes:\n""\n""    - foo()"},
    {NULL, NULL, 0, NULL}
};


#if PY_MAJOR_VERSION >= 3
  static struct PyModuleDef moduledef = {
    PyModuleDef_HEAD_INIT,
    "foo",            /* m_name */
    "",         /* m_doc */
    -1,                  /* m_size */
    Methods,             /* m_methods */
    NULL,                /* m_reload */
    NULL,                /* m_traverse */
    NULL,                /* m_clear */
    NULL,                /* m_free */
  };
#define PYTHRAN_RETURN return theModule
#define PYTHRAN_MODULE_INIT(s) PyInit_##s
#else
#define PYTHRAN_RETURN return
#define PYTHRAN_MODULE_INIT(s) init##s
#endif
PyMODINIT_FUNC
PYTHRAN_MODULE_INIT(foo)(void)
#ifndef _WIN32
__attribute__ ((visibility("default")))
#if defined(GNUC) && !defined(__clang__)
__attribute__ ((externally_visible))
#endif
#endif
;
PyMODINIT_FUNC
PYTHRAN_MODULE_INIT(foo)(void) {
    import_array()
    #if PY_MAJOR_VERSION >= 3
    PyObject* theModule = PyModule_Create(&moduledef);
    #else
    PyObject* theModule = Py_InitModule3("foo",
                                         Methods,
                                         ""
    );
    #endif
    if(! theModule)
        PYTHRAN_RETURN;
    PyObject * theDoc = Py_BuildValue("(sss)",
                                      "0.13.1",
                                      "2023-05-23 12:59:05.242803",
                                      "9c4469c517f668ea66a72a1351cd2183f764412f7e5f475130babb18001e4bf8");
    if(! theDoc)
        PYTHRAN_RETURN;
    PyModule_AddObject(theModule,
                       "__pythran__",
                       theDoc);

    PyModule_AddObject(theModule, "a", a);
    PYTHRAN_RETURN;
}

#endif