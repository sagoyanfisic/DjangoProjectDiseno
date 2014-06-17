<h1>Proyecto de Diseño de sistemas</h1> <br>

<font> Manual para la instalación de Framework Django</font> <br>

<font>Python tools</font><br>
<code>sudo apt-get install python-setuptools </code> <br>
<code> sudo apt-get install python-django</code><br>
<font>Inciar proyecto</font> <br>
<code> django-admin startproject nombreProyecto </code><br>
<code> cd nombreProyecto/ </code><br>
<code> python manage.py runserver </code><br>
<code>python manage.py syncdb </code><br>

<storge>Uso de South para hacer cambios en la BD y no perder datos en transcurso:</storge><br>
http://south.aeracode.org/<br>
<storge>Documentación de South:</storge><br>
http://south.readthedocs.org/en/latest/<br>

Iniciando la migración con south : <br>
<code>$ python manage.py schemamigration principal --initial</code> <br>
<code>$ python manage.py migrate principal </code>
