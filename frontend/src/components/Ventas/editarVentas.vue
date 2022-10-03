<template lang="html">
  <div class="container">

    <div class="row">
      <div class="col text-left">
        <h2>Editar venta</h2>
      </div>
    </div>

    <div class="row">
      <div class="col">
        <div class="card">
          <div class="card-body">

            <form @submit="onSubmit">

              <div class="form-group row">
                <label for="id_venta" class="col-sm-2 col-form-label">ID venta</label>
                <div class="col-sm-6">
                  <input type="text" placeholder="ID" name="id_venta" class="form-control" v-model.trim="form.id_venta">
                </div>
              </div>

              <div class="form-group row">
                <label for="fecha" class="col-sm-2 col-form-label">Fecha</label>
                <div class="col-sm-6">
                  <input type="date" placeholder="Fecha" name="fecha" class="form-control" v-model.trim="form.fecha">
                </div>
              </div>

              <div class="form-group row">
                <label for="cantidad" class="col-sm-2 col-form-label">Cantidad</label>
                <div class="col-sm-6">
                  <input type="number" placeholder="Cantidad" name="cantidad" class="form-control" v-model.trim="form.cantidad">
                </div>
              </div>

              <div class="form-group row">
                <label for="producto" class="col-sm-2 col-form-label">Producto</label>
                <div class="col-sm-6">
                  <input type="producto" placeholder="Producto" name="producto" class="form-control" v-model.trim="form.producto">
                </div>
              </div>

              <div class="rows">
                <div class="col text-left">
                  <b-button type="submit" variant="primary">Editar</b-button>
                  <b-button type="submit" class="btn-large-space" variant="danger" :to="{ name: 'listarVentas' }">Cancelar</b-button>
                  <b-button type="submit" class="btn-large-space" :to="{ name: 'listarVentas' }">Volver</b-button>
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
import axios from 'axios'
import swal from 'sweetalert'
export default {
  data() {
    return {
      id_venta: this.$route.params.id_venta,
      form: {
        id_venta:'',
        fecha: '',
        cantidad: '',
        producto: ''
      }
    }
  },
  methods: {
    onSubmit (evt) {
      evt.preventDefault()
      const path = `http://127.0.0.1:8000/api/v1.0/ventas/${this.id_venta}/`
      axios.put(path, this.form).then((response) => {
        this.form.id_venta = response.data.id_venta
        this.form.fecha = response.data.fecha
        this.form.cantidad = response.data.cantidad
        this.form.producto = response.data.producto
        swal("Venta actualizada existosamente!", "", "success")
      })
      .catch((error) => {
        console.log(error)
      })
      
    },
    getVenta (){
      const path = `http://127.0.0.1:8000/api/v1.0/ventas/${this.id_venta}/`
      axios.get(path).then((response) => {
        this.form.id_venta = response.data.id_venta
        this.form.fecha = response.data.fecha
        this.form.cantidad = response.data.cantidad
        this.form.producto = response.data.producto
      })
      .catch((error) => {
        console.log(error)
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