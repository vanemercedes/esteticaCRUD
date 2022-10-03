<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <h3>Base de datos de productos y ventas</h3>
    <h5>Links esenciales</h5>
    
    <ul>
      <li>
        <a
          href="http://localhost:8080/productos/nuevo"
          target="_blank"
        >
          Nuevo producto
        </a>
      </li>
      <li>
        <a
          href="http://localhost:8080/productos"
          target="_blank"
        >
          Listado de productos
        </a>
      </li>
      <li>
        <a
          href="http://localhost:8080/ventas/nuevo"
          target="_blank"
        >
          Nueva venta
        </a>
      </li>
      <li>
        <a
          href="http://localhost:8080/ventas"
          target="_blank"
        >
          Listado de ventas
        </a>
      </li>
      <br>
      
    
    </ul>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Bienvenido a Tatiana Pérez App'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #3eb0a7;
}
</style>
