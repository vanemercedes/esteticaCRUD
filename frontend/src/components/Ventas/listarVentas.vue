<template lang="html">
    <div class="container">
      <div class="row">
        <div class="col text-left">
          <div class="">
            <h2>Listado de ventas</h2>
            <b-button size="sm" :to="{name: 'nuevaVenta'}" variant="primary">
              Nueva venta
            </b-button>
          </div>
          <br>
          <div class="col-md-12">
            <b-table striped hover :items="ventas" :fields="fields">
  
              <template v-slot:cell(action)="data">
                <b-button size="sm" variant="primary" :to="{ name:'editarVentas', params: {id_venta: data.item.id_venta} }">
                  Editar
                </b-button>
                <b-button size="sm" variant="danger" :to="{ name:'eliminarVentas', params: {id_venta: data.item.id_venta} }">
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
            
          { key: 'id_venta', label: 'ID' },
          { key: 'fecha', label: 'Fecha' },
          { key: 'cantidad', label: 'Cantidad' },
          { key: 'producto', label: 'Producto' },
          { key: 'action', label: '' }
          
        ],
        ventas: []
      }
    },
    methods: {
      getVentas () {
        const path = 'http://127.0.0.1:8000/api/v1.0/ventas/'
        axios.get(path).then((response) => {
          this.ventas = response.data
        })
        .catch((error) => {
          console.log(error)
        })
      }
    },
    created(){
      this.getVentas()
    }
  }
  </script>
  
  <style lang="css" scoped>
  </style>