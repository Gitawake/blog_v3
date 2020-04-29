<template>
  <div class="hello">

  </div>
</template>

<script>
  const Axios = require('axios');
  export default {
    name: 'HelloWorld',
    data() {
      return {
        blog_class: []
      }
    },
    created() {
      Axios.get('http://127.0.0.1:8000/api/')
        .then(response => {
          console.log(response.data)
          this.blog_class = response.data.Content.blogclass
        })
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
