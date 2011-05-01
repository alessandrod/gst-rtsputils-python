SUBDIRS = codegen
pkgpyexecdir = $(pyexecdir)/gst-$(GST_MAJORMINOR)/gst

# we install everything in pyexecdir; otherwise you end up with a mess for
# multilib
pygstrtsputilsdir = $(pkgpyexecdir)
pygstrtsputils_PYTHON =

pygstrtsputilsexecdir = $(pkgpyexecdir)
pygstrtsputilsexec_LTLIBRARIES = _rtsputils.la

DEFS = $(srcdir)/rtsputils-types.defs $(srcdir)/rtsputils.defs
defs_DATA = $(DEFS)
defsdir = $(pkgdatadir)/$(GST_MAJORMINOR)/defs
OVERRIDES = rtsputils.override

INCLUDES = -I$(top_srcdir) -I$(srcdir) $(PYTHON_INCLUDES)

_rtsputils_la_CFLAGS = -I$(top_srcdir)/src \
		$(PYGOBJECT_CFLAGS) $(GST_PLUGINS_BASE_CFLAGS) $(GST_CFLAGS) \
		-I$(top_srcdir)/gst-rtsp-cam/src
_rtsputils_la_LDFLAGS = -export-symbols-regex "^(init_rtsputils|_PyGObject_API).*" \
	-module -avoid-version $(GST_PLUGIN_LDFLAGS)
_rtsputils_la_LIBADD = \
		$(GST_PLUGINS_BASE_LIBS) $(GST_BASE_LIBS) \
		-lgstrtp-@GST_MAJORMINOR@ -lgstrtsp-@GST_MAJORMINOR@ \
        	-lgstsdp-@GST_MAJORMINOR@ $(GST_LIBS) $(LIBM) \
		$(top_srcdir)/gst-rtsp-cam/src/libgstrtspcam.la
_rtsputils_la_SOURCES = rtsputilsmodule.c 
nodist__rtsputils_la_SOURCES = rtsputils.c

EXTRA_DIST = $(defs_DATA) $(OVERRIDES) arg-types.py

CLEANFILES = rtsputils.c

rtsputils.c: $(DEFS) $(OVERRIDES) arg-types.py

.defs.c: 
	($(PYTHON) $(srcdir)/codegen/codegen.py \
		--load-types $(srcdir)/arg-types.py \
		--register $(srcdir)/rtsputils-types.defs \
		--register $(PYGST_DEFSDIR)/gst-types.defs \
		--override $(srcdir)/$*.override \
		--extendpath $(top_builddir)/src/ \
		--extendpath $(srcdir)/ \
		--prefix pygst_rtsp_utils $<) > gen-$*.c \
	&& cp gen-$*.c $*.c \
	&& rm -f gen-$*.c
