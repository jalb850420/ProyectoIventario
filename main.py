import os
from flask import Flask, request, render_template, redirect, url_for, flash
from flask import g

from database import sql_select_usuarios,sql_select_proveedores, sql_insert_tipousuario, sql_select_productos, sql_delete_productos , sql_edit_productos, sql_actualizar_producto, sql_consulta_login
from forms import  TipoUsuario,Producto, EditProducto
app = Flask(__name__)
#app.secret_key = os.urandom(24)
app.secret_key ='mysecretkey'

@app.route('/', methods=["GET","POST"])
def Home():
   return render_template('home.html')

#CRUD OK***************************************************
#                    CONSULTA PARA LOGIN
#CRUD OK***************************************************

@app.route('/Inicio', methods=["GET","POST"])
def Inicio():
   g.nombre = request.form.get("nombre")
   g.clave = request.form.get("clave")
   valor = sql_consulta_login(g.nombre, g.clave)
   print(valor)
   if len(valor) == 0: 
      flash('Usuario o contraseña incorrecta!')
      return render_template('home.html')
   else:
      return render_template('inicio.html', nombre=g.nombre, clave = g.clave)

#CRUD OK***************************************************
#                  PRODUCTO
#CRUD OK***************************************************
#                 NUEVO



#                 ACTUALIZAR

@app.route('/edit/<id>', methods=['GET'])
def editar_producto(id):
   form=EditProducto()
   data = sql_edit_productos(id)
   return render_template('editProducto.html',data = data, form = form)

@app.route('/actualizar/<id>', methods=['POST'])
def actualizar_producto(id):
   if  request.method == "POST": #Si la ruta es accedida a través del método POST entonces
      idp = request.form["IdProducto"] #captura de la variable id enviada a través de la URL
      nomproducto = request.form["NombreProducto"] #captura de la vble código enviada a través de la URL
      marcaproducto = request.form["MarcaProducto"] #captura de la vble nombre enviada a través de la URL
      descripproducto = request.form["DescripProducto"] #captura de la vble cantidad enviada a través de la URL
      costoproducto = request.form["CostoProducto"] #captura de la variable id enviada a través de la URL
      precio = request.form["Precio"] #captura de la vble código enviada a través de la URL
      cantidad = request.form["Cantidad"] #captura de la vble nombre enviada a través de la URL
      idprov = request.form["IdProv"] #captura de la vble cantidad enviada a través de la URL
      idcategoria = request.form["IdCategoria"] #captura de la vble cantidad enviada a través de la URL
      sql_actualizar_producto(idp, nomproducto, marcaproducto, descripproducto, costoproducto, precio, cantidad, idprov, idcategoria, id) #llamado de la función de edición de la base de datos
      return redirect(url_for('productos'))

#                 MOSTRAR
@app.route('/Mostrarproductos', methods=['GET', 'POST']) 
def mostrar_productos(): 
   products = sql_select_productos()
   return render_template('productos.html', products=products)

#                 DELETE

@app.route('/delete/<id>')
def borrar_producto(id):
   sql_delete_productos(id) #llamado a la función de borrado de la base de datos
   return redirect(url_for('productos'))

#CRUD OK***************************************************
#                  USUARIO
#CRUD OK***************************************************
#                   NUEVO

@app.route('/Insertar/Usuarios', methods=['GET', 'POST'])
def nuevousuario():
   if  request.method == "GET": #Si la ruta es accedida a través del método GET entonces
	   form = TipoUsuario() #Crea un nuevo formulario de tipo producto
	   return render_template('nuevo_Tipo_Usuario.html', form=form) #redirecciona vista nuevo html enviando la variable form
   if request.method == "POST": #Si la ruta es accedida a través del método POST entonces
      cod = request.form["codigo"] #asigna variable cod con valor enviado desde formulario  en la vista html
      nom = request.form["nombre"] #asigna variable nom con valor enviado desde formulario en la vista html
      sql_insert_tipousuario(cod, nom) #llamado de la función para insertar el nuevo producto
      flash('Dato almacenado con exito!')
      return redirect(url_for('nuevousuario'))


#                 ACTUALIZAR


#                 MOSTRAR
@app.route('/MostrarUsuarios', methods=['GET', 'POST']) 
def mostrar_usuario(): 
   User = sql_select_usuarios()
   return render_template('usuario.html', User = User)

#                 DELETE
#CRUD OK***************************************************
#                TIPO DE USUARIO
#CRUD OK***************************************************
#                   NUEVO

@app.route('/nuevo_Tipo_Usuario', methods=['GET', 'POST'])
def nuevotipousuario():
   if  request.method == "GET": #Si la ruta es accedida a través del método GET entonces
	   form = TipoUsuario() #Crea un nuevo formulario de tipo producto
	   return render_template('nuevo_Tipo_Usuario.html', form=form) #redirecciona vista nuevo html enviando la variable form
   if request.method == "POST": #Si la ruta es accedida a través del método POST entonces
      cod = request.form["codigo"] #asigna variable cod con valor enviado desde formulario  en la vista html
      nom = request.form["nombre"] #asigna variable nom con valor enviado desde formulario en la vista html
      sql_insert_tipousuario(cod, nom) #llamado de la función para insertar el nuevo producto
      flash('Dato almacenado con exito!')
      return redirect(url_for('nuevotipousuario'))


#                 ACTUALIZAR


#                 MOSTRAR


#                 DELETE

#CRUD OK***************************************************
#                  PROVEEDORES
#CRUD OK***************************************************
#                   NUEVO

#                 ACTUALIZAR


#                  MOSTRAR
@app.route('/MostrarProveedores', methods=['GET', 'POST']) 
def mostrar_proveedores(): 
   supplier = sql_select_proveedores()
   return render_template('proveedores.html', supplier = supplier)

#                   DELETE

#-------------------------------
#           MY SQL
#-------------------------------
#@app.route('/Usuarios')
#def Usuario():
#   cursor = mysql.connection.cursor()
#   cursor.execute(' SELECT * FROM usuarios  ')
#   user = cursor.fetchall()
#   cursor.close()
#   return render_template('usuario.html', user = user)

#-------------------------------
#@app.route('/Productos')
#def Productos():
#   cursor = mysql.connection.cursor()
#   cursor.execute(' SELECT * FROM Productos  ')
#   products = cursor.fetchall()
#   cursor.close()
#   return render_template('productos.html', products = products)

#-------------------------------
#@app.route('/Proveedores')
#def Proveedores():
#   cursor = mysql.connection.cursor()
#   cursor.execute(' SELECT * FROM Proveedores  ')
#   supplier = cursor.fetchall()
#   cursor.close()
#   return render_template('proveedores.html', supplier = supplier)
#-------------------------------