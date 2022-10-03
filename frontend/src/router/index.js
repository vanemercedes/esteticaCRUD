import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import nuevoProducto from '@/components/Producto/nuevoProducto'
import listarProductos from '@/components/Producto/listarProductos'
import editarProductos from '@/components/Producto/editarProductos'
import eliminarProductos from '@/components/Producto/eliminarProductos'
import nuevaVenta from '@/components/ventas/nuevaVenta'
import listarVentas from '@/components/ventas/listarVentas'
import editarVentas from '@/components/ventas/editarVentas'
import eliminarVentas from '@/components/ventas/eliminarVentas'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    }, {
      path: '/productos',
      name: 'listarProductos',
      component: listarProductos
    },
    {
      path: '/productos/nuevo',
      name: 'nuevoProducto',
      component: nuevoProducto
    },
    {
      path: '/productos/:id_producto/editar',
      name: 'editarProductos',
      component: editarProductos
    }, 
    {
      path: '/productos/:id_producto/eliminar',
      name: 'eliminarProductos',
      component: eliminarProductos
    }, 
    {
      path: '/ventas',
      name: 'listarVentas',
      component: listarVentas
    },
    {
      path: '/ventas/nuevo',
      name: 'nuevaVenta',
      component: nuevaVenta
    },
    {
      path: '/ventas/:id_venta/editar',
      name: 'editarVentas',
      component: editarVentas
    },
    {
      path: '/ventas/:id_venta/eliminar',
      name: 'eliminarVentas',
      component: eliminarVentas
    }     
    
  ],
  mode:'history'
})
