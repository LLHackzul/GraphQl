<template>
  <div>
    <ul>
        <li :key="carro.id" v-for="carro  in carros.data.allCars" >
          {{carro.name}} {{carro.line}} {{carro.model}}
        </li>
    </ul>    
  </div>
</template>
    
 
<script>

import gql from 'graphql-tag'

  export default {
    name: 'CarList',    
    //definimos la variable que almacenara el listado de ingredientes
    data () {
      return {
        carros: ''
      }
    },    

    //declaramos un metodo que vaya a leer los ingredientes a GraphQl
    methods:
    {
      // sera un funcion asincrona pues debera esperar hasta recibir la respuesta externa
      async leerCarros(){
        
        //desde aquí se realiza la consulta a Graphql y el resultado se guarda en una constante
        const ingredientesGraphql = await this.$apollo.query({
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
        this.carros = ingredientesGraphql
        

      }      

    },
    //el metodo leerIngredientes se ejecutara cada vez que los componentes de la pagina ya esten montados
    mounted () {
      this.leerCarros()
    }
    
  }
  
</script>