<template>
  <div>
    <div :key="categoria.id" v-for="categoria  in categorias.data.allCategories">
        <h2>{{categoria.name}}</h2>
        <ul>
            <li :key="carro.id" v-for="carro  in categoria.cars">
                <strong> Marca:</strong> {{carro.name}} <strong> Línea:</strong> {{carro.line}} <strong> Color:</strong> {{carro.color}}  <strong> Modelo:</strong> {{carro.model}}
            </li>
        </ul>
    </div>
      
  </div>
</template>
    
 
<script>

import gql from 'graphql-tag'

  export default {
    name: 'CarList',    
    //definimos la variable que almacenara el listado de ingredientes
    data () {
      return {
        carros: '',
        categorias: ''
      }
    },    

    //declaramos un metodo que vaya a leer los ingredientes a GraphQl
    methods:
    {
      // sera un funcion asincrona pues debera esperar hasta recibir la respuesta externa
      async leerCarros(){
        
        //desde aquí se realiza la consulta a Graphql y el resultado se guarda en una constante
        const carrosGraphql = await this.$apollo.query({
        query: gql`query {
                   allCars {
                        name,
                        line,
                        color,
                        model,
                        category {
                        name
                        }
                    }
                  }`,     
        })

        //El dato obtenido de Graphql se lo asignamos a la variable ingredientes que se mostrara en el template
        this.carros = carrosGraphql
        

      },
      async leerCategorias(){
          const categoriasGraphql = await this.$apollo.query({
        query: gql`query {
  allCategories {
    name
    cars {
      name,
      line,
			color,
			model,
    }
  }
}`,     
        })

        //El dato obtenido de Graphql se lo asignamos a la variable ingredientes que se mostrara en el template
        this.categorias = categoriasGraphql
        
      }      

    },
    //el metodo leerIngredientes se ejecutara cada vez que los componentes de la pagina ya esten montados
    mounted () {
      this.leerCarros(),
       this.leerCategorias()
    }
    
  }
  
</script>