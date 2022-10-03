<template lang="html">
    <div class="container">
      <div class="row">
        <div class="col text-left">
          <div class="">
            <h2>Listado de productos</h2>
            <b-button size="sm" :to="{name: 'nuevoProducto'}" variant="primary">
              Nuevo producto
            </b-button>
          </div>
          <br>
          <div class="col-md-12">
            <b-table striped hover :items="productos" :fields="fields">
  
              <template v-slot:cell(action)="data">
                <b-button size="sm" variant="primary" :to="{ name:'editarProductos', params: {id_producto: data.item.id_producto} }">
                  Editar
                </b-button>
                <b-button size="sm" variant="danger" :to="{ name:'eliminarProductos', params: {id_producto: data.item.id_producto} }">
                  Eliminar
                </b-button>
              </template>
  
            </b-table>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  export default {
    data () {
      return {
        
        fields: [
            
          { key: 'id_producto', label: 'ID' },
          { key: 'nombreProd', label: 'Nombre' },
          { key: 'precioProd', label: 'Precio' },
          { key: 'nombreProd', label: 'Nombre' },
          { key: 'descripcionProd', label: 'Descripción' },
          { key: 'action', label: '' }
        ],
        productos: []
      }
    },
    methods: {
      getProductos () {
        const path = 'http://127.0.0.1:8000/api/v1.0/productos/'
        axios.get(path).then((response) => {
          this.productos = response.data
        })
        .catch((error) => {
          console.log(error)
        })
      }
    },
    created(){
      this.getProductos()
    }
  }
  </script>
  
  <style lang="css" scoped>
  </style>