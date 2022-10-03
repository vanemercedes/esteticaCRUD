<template lang="html">
    <div class="container">
      <div class="row">
        <div class="col">
  
          <h3>¿Estas seguro que deseas eliminar esta venta?</h3>
          <p>ID venta : {{ this.element.id_venta }}</p>
          <p>Fecha : {{ this.element.fecha }}</p>
          <p>Cantidad : {{ this.element.cantidad }}</p>
          <p>Producto : {{ this.element.producto }}</p>
          
        </div>
      </div>
  
      <div class="row">
        <div class="col">
          <b-button v-on:click="borrarVenta" variant="danger">Eliminar</b-button>
          <b-button type="submit" class="btn-large-space" :to="{ name: 'listarVentas' }">Volver</b-button>
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
        id_venta: this.$route.params.id_venta,
        element: {
          id_venta: '',
          fecha: '',
          cantidad: '',
          producto: ''
        }
      }
    },
    methods: {
      getVenta (){
        const path = `http://127.0.0.1:8000/api/v1.0/ventas/${this.id_venta}/`
        axios.get(path).then((response) => {
          this.element.id_venta = response.data.id_venta
          this.element.fecha = response.data.fecha
          this.element.cantidad = response.data.cantidad
          this.element.producto = response.data.producto
        })
        .catch((error) => {
          console.log(error)
        })
      },
      borrarVenta () {
        const path = `http://127.0.0.1:8000/api/v1.0/ventas/${this.id_venta}/`
        axios.delete(path).then((response) => {
          location.href = '/ventas'
        })
        .catch((error) => {
          swal("No es posible eliminar la venta", "", "error")
        })
      }
    },
    created() {
      this.getVenta()
    }
  }
  </script>
  
  <style lang="css" scoped>
  </style>