AC_PREREQ(2.52)
AC_INIT(GStreamer-RTSP-Python, 0.10.0.1)
AM_CONFIG_HEADER([config.h])
AC_CANONICAL_TARGET
AM_INIT_AUTOMAKE
dnl can autoconf find the source ?
dnl AC_CONFIG_SRCDIR([src/g.c])
AC_LIBTOOL_WIN32_DLL
AM_PROG_LIBTOOL
AC_PROG_CC
AM_PROG_CC_C_O
AM_PROG_AS
PKG_PROG_PKG_CONFIG
GST_REQ=0.10.18
PKG_CHECK_MODULES(GST, gstreamer-0.10)
PKG_CHECK_MODULES(GST_RTSP_SERVER, gst-rtsp-server-0.10)
AM_CHECK_PYTHON_HEADERS([HAVE_PYTHON_HEADERS=yes],[HAVE_PYTHON_HEADERS=no])
PYGOBJECT_REQ=2.11.2
PKG_CHECK_MODULES(PYGOBJECT, pygobject-2.0 >= $PYGOBJECT_REQ,
  [HAVE_PYGOBJECT="yes"], [HAVE_PYGOBJECT="no"])
AC_SUBST(PYGOBJECT_CFLAGS)
dnl check for gst-python
PKG_CHECK_MODULES(PYGST, gst-python-0.10,
  [HAVE_PYGST="yes"], [HAVE_PYGST="no"])

if test "x$HAVE_PYGST" = "xyes"; then
  PYGST_DEFSDIR=`pkg-config gst-python-0.10 --variable=defsdir`
fi
GST_MAJORMINOR=0.10
AC_SUBST(GST_MAJORMINOR)
AC_SUBST(PYGST_DEFSDIR, $PYGST_DEFSDIR)
AC_CONFIG_FILES(
Makefile
rtsputils/Makefile
rtsputils/codegen/Makefile
gst-rtsp-cam/Makefile
gst-rtsp-cam/src/Makefile
gst-rtsp-relay/Makefile
gst-rtsp-relay/src/Makefile
)
AC_OUTPUT
