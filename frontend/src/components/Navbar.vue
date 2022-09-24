<template>
  <div>
      <nav aria-label="nav bar" tabindex="0" class="focus:outline-none w-full bg-gray-800 hidden xl:block shadow">
          <div class="container px-6 h-16 flex justify-between items-center lg:items-stretch mx-auto">
              <div class="flex items-center">
                  <div tabindex="0" class="focus:outline-none mr-10 flex items-center">
                      <img src="https://tuk-cdn.s3.amazonaws.com/can-uploader/black-left-aligned-with-search-bar-icons-svg1.svg" alt="north" />
                      <h3 class="text-base text-white font-bold tracking-normal leading-tight ml-3 hidden lg:block">The Свинюшка Жоры</h3>
                  </div>    
              </div>
              <div>
                <form class="mt-3 flex items-center">
                  <label class="block">
                    <input accept=".csv" type="file" class="block w-full text-sm text-slate-500
                      file:mr-4 file:py-2 file:px-4
                      file:rounded-full file:border-0
                      file:text-sm file:font-semibold
                      file:bg-violet-50 file:text-violet-700
                      hover:file:bg-violet-100
                    " ref="file" v-on:change="handleFileUpload()" />
                  </label>
                  <button class="bg-violet-50 hover:bg-violet-100 text-violet-700 font-bold ml-3 py-2 px-3 rounded-full" @click="submitFile()">
                    Загрузить  
                  </button>
                </form>
              </div>
          </div>
      </nav>
    </div>
</template>

<script>
import  axios from 'axios'
export default {
  data(){
      return {
        file: ''
      }
    },
  methods: {
      submitFile(){
            let formData = new FormData();
            formData.append('file', this.file);
            axios.post( 'http://127.0.0.1:8000/main/load_file/',
                formData,
                {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
              }
            ).then(function(){
          console.log('SUCCESS!!');
        })
        .catch(function(){
          console.log('FAILURE!!');
        });
      },
      handleFileUpload(){
        this.file = this.$refs.file.files[0];
      }
    }
  }
</script>

<style>

</style>