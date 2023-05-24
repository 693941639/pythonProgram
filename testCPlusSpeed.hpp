#define PY_MAJOR_VERSION 3
#undef ENABLE_PYTHON_MODULE
#include <pythonic/core.hpp>
#include <pythonic/python/core.hpp>
#include <pythonic/types/bool.hpp>
#include <pythonic/types/int.hpp>
#ifdef _OPENMP
#include <omp.h>
#endif
#include <pythonic/include/types/int.hpp>
#include <pythonic/types/int.hpp>
#include <pythonic/include/builtins/int_.hpp>
#include <pythonic/include/operator_/add.hpp>
#include <pythonic/include/operator_/lt.hpp>
#include <pythonic/include/operator_/sub.hpp>
#include <pythonic/builtins/int_.hpp>
#include <pythonic/operator_/add.hpp>
#include <pythonic/operator_/lt.hpp>
#include <pythonic/operator_/sub.hpp>
namespace 
{
  namespace __pythran_testCPlusSpeed
  {
    struct fib
    {
      typedef void callable;
      typedef void pure;
      template <typename argument_type0 >
      struct type
      {
        typedef typename std::remove_cv<typename std::remove_reference<argument_type0>::type>::type __type0;
        typedef __type0 __type1;
        typedef decltype(pythonic::operator_::add(std::declval<__type1>(), std::declval<__type1>())) __type2;
        typedef typename __combined<__type1,__type2>::type __type3;
        typedef typename pythonic::returnable<__type3>::type __type4;
        typedef __type4 result_type;
      }  
      ;
      template <typename argument_type0 >
      inline
      typename type<argument_type0>::result_type operator()(argument_type0 n) const
      ;
    }  ;
    template <typename argument_type0 >
    inline
    typename fib::type<argument_type0>::result_type fib::operator()(argument_type0 n) const
    {
      if (pythonic::operator_::lt(n, 2L))
      {
        return n;
      }
      else
      {
        return pythonic::operator_::add(pythonic::types::call(fib(), pythonic::operator_::sub(n, 1L)), pythonic::types::call(fib(), pythonic::operator_::sub(n, 2L)));
      }
    }
  }
}
#include <pythonic/python/exception_handler.hpp>
#ifdef ENABLE_PYTHON_MODULE
inline
typename __pythran_testCPlusSpeed::fib::type<long>::result_type fib0(long&& n) 
{
  
                            PyThreadState *_save = PyEval_SaveThread();
                            try {
                                auto res = __pythran_testCPlusSpeed::fib()(n);
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
__pythran_wrap_fib0(PyObject *self, PyObject *args, PyObject *kw)
{
    PyObject* args_obj[1+1];
    
    char const* keywords[] = {"n",  nullptr};
    if(! PyArg_ParseTupleAndKeywords(args, kw, "O",
                                     (char**)keywords , &args_obj[0]))
        return nullptr;
    if(is_convertible<long>(args_obj[0]))
        return to_python(fib0(from_python<long>(args_obj[0])));
    else {
        return nullptr;
    }
}

            static PyObject *
            __pythran_wrapall_fib(PyObject *self, PyObject *args, PyObject *kw)
            {
                return pythonic::handle_python_exception([self, args, kw]()
                -> PyObject* {

if(PyObject* obj = __pythran_wrap_fib0(self, args, kw))
    return obj;
PyErr_Clear();

                return pythonic::python::raise_invalid_argument(
                               "fib", "\n""    - fib(int)", args, kw);
                });
            }


static PyMethodDef Methods[] = {
    {
    "fib",
    (PyCFunction)__pythran_wrapall_fib,
    METH_VARARGS | METH_KEYWORDS,
    "Supported prototypes:\n""\n""    - fib(int)"},
    {NULL, NULL, 0, NULL}
};


#if PY_MAJOR_VERSION >= 3
  static struct PyModuleDef moduledef = {
    PyModuleDef_HEAD_INIT,
    "testCPlusSpeed",            /* m_name */
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
PYTHRAN_MODULE_INIT(testCPlusSpeed)(void)
#ifndef _WIN32
__attribute__ ((visibility("default")))
#if defined(GNUC) && !defined(__clang__)
__attribute__ ((externally_visible))
#endif
#endif
;
PyMODINIT_FUNC
PYTHRAN_MODULE_INIT(testCPlusSpeed)(void) {
    import_array()
    #if PY_MAJOR_VERSION >= 3
    PyObject* theModule = PyModule_Create(&moduledef);
    #else
    PyObject* theModule = Py_InitModule3("testCPlusSpeed",
                                         Methods,
                                         ""
    );
    #endif
    if(! theModule)
        PYTHRAN_RETURN;
    PyObject * theDoc = Py_BuildValue("(sss)",
                                      "0.13.1",
                                      "2023-05-24 10:35:35.960815",
                                      "36d588cb9f71edad6f14e9197cb58aab9da91eb2271e342075eb87a0278d65ba");
    if(! theDoc)
        PYTHRAN_RETURN;
    PyModule_AddObject(theModule,
                       "__pythran__",
                       theDoc);


    PYTHRAN_RETURN;
}

#endif