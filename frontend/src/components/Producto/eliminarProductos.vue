<template lang="html">
    <div class="container">
      <div class="row">
        <div class="col">
  
          <h3>¿Estas seguro que deseas eliminar este producto?</h3>
          <p>Nombre : {{ this.element.nombreProd }}</p>
          <p>Precio : {{ this.element.precioProd }}</p>
          <p>Contenido : {{ this.element.contenido }}</p>
          <p>Descripción : {{ this.element.descripcionProd }}</p>
  
        </div>
      </div>
  
      <div class="row">
        <div class="col">
          <b-button v-on:click="borrarProducto" variant="danger">Eliminar</b-button>
          <b-button type="submit" class="btn-large-space" :to="{ name: 'listarProductos' }">Volver</b-button>
        </div>
      </div>
  
    </div>
  
  </template>
  
  <script>
  import axios from 'axios';
  import swal from 'sweetalert'
  export default {
    data () {
      return {
        id_producto: this.$route.params.id_producto,
        element: {
          nombreProd: '',
          precioProd: '',
          contenido: '',
          descripcion: ''
        }
      }
    },
    methods: {
      getProducto (){
        const path = `http://127.0.0.1:8000/api/v1.0/productos/${this.id_producto}/`
        axios.get(path).then((response) => {
          this.element.nombreProd = response.data.nombreProd
          this.element.precioProd = response.data.precioProd
          this.element.contenido = response.data.contenido
          this.element.descripcionProd = response.data.descripcionProd
        })
        .catch((error) => {
          console.log(error)
        })
      },
      borrarProducto () {
        const path = `http://127.0.0.1:8000/api/v1.0/productos/${this.id_producto}/`
        axios.delete(path).then((response) => {
          location.href = '/productos'
        })
        .catch((error) => {
          swal("No es posible eliminar el producto", "", "error")
        })
      }
    },
    created() {
      this.getProducto()
    }
  }
  </script>
  
  <style lang="css" scoped>
  </style>