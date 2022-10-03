<template lang="html">
    <div class="container">
  
      <div class="row">
        <div class="col text-left">
          <h2>Nuevo producto</h2>
        </div>
      </div>
  
      <div class="row">
        <div class="col">
          <div class="card">
            <div class="card-body">
  
              <form @submit="onSubmit">
  
                <div class="form-group row">
                  <label for="nombreProd" class="col-sm-2 col-form-label">Nombre</label>
                  <div class="col-sm-6">
                    <input type="text" placeholder="Producto" name="nombreProd" class="form-control" v-model.trim="form.nombreProd">
                  </div>
                </div>

                <div class="form-group row">
                  <label for="precioProd" class="col-sm-2 col-form-label">Precio</label>
                  <div class="col-sm-6">
                    <input type="text" placeholder="Precio" name="precioProd" class="form-control" v-model.trim="form.precioProd">
                  </div>
                </div>

                <div class="form-group row">
                  <label for="contenido" class="col-sm-2 col-form-label">Contenido</label>
                  <div class="col-sm-6">
                    <input type="text" placeholder="Contenido neto" name="contenido" class="form-control" v-model.trim="form.contenido">
                  </div>
                </div>
  
                <div class="form-group row">
                  <label for="descripcionProd" class="col-sm-2 col-form-label">Descripción</label>
                  <div class="col-sm-6">
                    <textarea name="descripcionProd" class="form-control" placeholder="Descripción" rows="3" v-model.trim="form.descripcionProd">
                    </textarea>
                  </div>
                </div>
  
                <div class="rows">
                  <div class="col text-left">
                    <b-button type="submit" variant="primary">Crear</b-button>
                    <b-button type="submit" class="btn-large-space" variant="danger" :to="{ name: 'listarProductos' }">Cancelar</b-button>
                    <b-button type="submit" class="btn-large-space" :to="{ name: 'listarProductos' }">Volver</b-button>
                  </div>
                </div>
  
              </form>
  
            </div>
          </div>
        </div>
      </div>
  
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import swal from 'sweetalert'
  export default {
    data() {
      return {
        form: {
          nombreProd: '',
          precioProd: '',
          contenido: '',
          descripcionProd: ''
        }
      }
    },
    methods: {
      onSubmit (evt) {
        evt.preventDefault()
        const path = 'http://127.0.0.1:8000/api/v1.0/productos/'
        axios.post(path, this.form).then((response) => {
          this.form.nombreProd = response.data.nombreProd
          this.form.precioProd = response.data.precioProd
          this.form.contenido = response.data.contenido
          this.form.descripcionProd = response.data.descripcionProd
          swal("Producto creado existosamente!", "", "success")
        })
        .catch((error) => {
          swal("El producto no ha sido creado", "", "error")
        })
      },
    },
    created() {
      
    }
  }
  </script>
  
  <style lang="css" scoped>
  </style>