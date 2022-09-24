<template>
<div><Navbar></Navbar>
   <div class="bg-gradient-to-r from-cyan-500 to-pink-500">
   <div class="px-64">
    <div class="w-full h-screen bg-opacity-25 backdrop-blur bg-white/30 rounded shadow-2xl">
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
      <div class="flex justify-center filearea">
        <span class="py-8 flex text-4xl font-bold font-corme">
          Рассматриваемый файл:
        </span>
      </div>
      <div class="grid grid-cols-3 col-auto mr-12">
        <div class="max-w-sm w-full lg:max-w-full lg:flex">
           <div class="h-48 lg:h-auto lg:w-12 flex-none bg-cover rounded-t lg:rounded-t-none lg:rounded-l text-center overflow-hidden">
           </div>
           <div class="border-r border-b border-l w-full shadow-xl hover:shadow-2xl border-gray-400 lg:border-l-0 lg:border-t lg:border-gray-400 bg-white rounded-b lg:rounded-b-none lg:rounded-r p-4 flex flex-col justify-between leading-normal">
              <div class="mb-8">
                 <div iv class="text-gray-900 font-bold text-3xl mb-2 font-corme text-center">Подсчет запросов к таблицам</div>
                 <p class="text-gray-700 text-xl font-rale text-center">Позволяет проанализировать общее количество запросов к таблице.</p>
              </div>
           </div>
        </div>
        <div class="max-w-sm w-full lg:max-w-full lg:flex">
          <div class="h-48 lg:h-auto lg:w-12 flex-none bg-cover rounded-t lg:rounded-t-none lg:rounded-l text-center overflow-hidden" >
          </div>
          <div class="border-r border-b border-l w-full shadow-xl hover:shadow-2xl border-gray-400 lg:border-l-0 lg:border-t lg:border-gray-400 bg-white rounded-b lg:rounded-b-none lg:rounded-r p-4 flex flex-col justify-between leading-normal">
             <div class="mb-8">
                <div iv class="text-gray-900 font-bold text-3xl mb-2 font-corme text-center">Подсчет по запросам от разработчиков</div>
                <p class="text-gray-700 text-xl font-rale text-center">Позволяет выявить наиболее активных разработчиков, и тех кто единожды загрузил данные</p>
             </div>
          </div>
       </div>
       <div class="max-w-sm w-full lg:max-w-full lg:flex">
        <div class="h-48 lg:h-auto lg:w-12 flex-none bg-cover rounded-t lg:rounded-t-none lg:rounded-l text-center overflow-hidden">
        </div>
        <div class="border-r border-b border-l w-full shadow-xl hover:shadow-2xl border-gray-400 lg:border-l-0 lg:border-t lg:border-gray-400 bg-white rounded-b lg:rounded-b-none lg:rounded-r p-4 flex flex-col justify-between leading-normal">
           <div class="mb-8">
              <div iv class="text-gray-900 font-bold text-3xl mb-2 font-corme text-center">Функция 3</div>
              <p class="text-gray-700 text-xl font-rale text-center">Ждите, скоро появится ^_^</p>
           </div>
        </div>
     </div>
     </div>
     <div class="grid grid-cols-1">
      <!-- Snippet -->
<div class="flex justify-center text-gray-600">
    <div class="w-3/4 p-4 sm:px-6">
        <!-- Chart widget -->
        <div class="flex w-full flex-col col-span-full xl:col-span-8 bg-white shadow-lg rounded-sm border border-gray-200">
            <header class="px-5 py-4 border-b border-gray-100 items-center">
                <h2 class="font-bold text-3xl text-gray-800 text-center font-rale tracking-widest">Общее описание логов</h2>
            </header>
            <div class="flex justify-center px-1 py-2 ml-16">
                <div class="flex">
                    <!-- Unique Visitors -->
                    <div class="flex items-center py-2 mr-6">
                        <div class="mr-1">
                            <div class="flex items-center justify-center">
                                <div class="text-3xl font-bold text-gray-800 mr-2">24.7K</div>
                            </div>
                            <div class="text-lg text-gray-500 font-corme">Количество запросов к таблицам</div>
                        </div>
                    </div>
                    <!-- Total Pageviews -->
                    <div class="flex items-center py-2 mr-6">
                        <div class="mr-1">
                            <div class="flex items-center justify-center">
                                <div class="text-3xl font-bold text-gray-800 mr-2">56.9K</div>
                            </div>
                            <div class="text-lg text-gray-500 font-corme">Количество запросов разработчиков</div>
                        </div>
                    </div>
                    <!-- Bounce Rate -->
                    <div class="flex items-center py-2">
                        <div class="mr-5">
                            <div class="flex items-center justify-center">
                                <div class="text-3xl font-bold text-gray-800 mr-2">54K</div>
                                <div class="text-sm font-medium text-yellow-500"></div>
                            </div>
                            <div class="text-lg text-gray-500 font-corme">Количество запросов загрузчиков</div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- Chart built with Chart.js 3 -->
            <div class="flex justify-start mb-3 ml-12">
                <Scatter
    :chart-options="chartOptions"
    :chart-data="chartData"
    :chart-id="chartId"
    :dataset-id-key="datasetIdKey"
    :plugins="plugins"
    :css-classes="cssClasses"
    :styles="styles"
    :width="width"
    :height="height"
  />
                <div class="container">
                    <div class ="flex justify-center mt-32">
                        <p class="font-semibold text-xl font-corme tracking-widest">Самая используемая таблица</p>
                    </div>
                    <div class="flex justify-center">
                        <p class="font-semibold text-6xl font-rale tracking-widest hover:underline">2048 записей</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
</div>
     </div>
    </div>
   </div>
   </div>
</template>

<script>
import axios from 'axios'
import Navbar from '../components/Navbar.vue';
import BarChart from '../components/charts/BarChart.vue';
import { Scatter } from 'vue-chartjs'

import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  LineElement,
  CategoryScale,
  PointElement,
  LinearScale
} from 'chart.js'

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  LineElement,
  CategoryScale,
  PointElement,
  LinearScale
)

export default {
components: { Navbar, Scatter },
props: {
    chartId: {
      type: String,
      default: 'scatter-chart'
    },
    datasetIdKey: {
      type: String,
      default: 'label'
    },
    width: {
      type: Number,
      default: 400
    },
    height: {
      type: Number,
      default: 400
    },
    cssClasses: {
      default: '',
      type: String
    },
    styles: {
      type: Object,
      default: () => {}
    },
    plugins: {
      type: Array,
      default: () => []
    },
    
  },
data()
{
      return {

        tables1: '',
        from: '',
        into:'',
        join:'',
        chartData: {
        datasets: [
          {
            label: 'JOIN',
            fill: false,
            borderColor: '#887BB5',
            backgroundColor: '#4528A4',
            data:  [this.join]
            
          },
          {
            label: 'INTO',
            fill: false,
            borderColor: '#f87979',
            backgroundColor: '#FF3F3F',
            data: [
            ]
          },
          {
            label: 'FROM',
            fill: false,
            borderColor: '#23D323',
            backgroundColor: '#23D323',
            data: [
              {
                x: -2,
                y: -4
              },
              {
                x: -1,
                y: -1
              },
              {
                x: 0,
                y: 1
              },
              {
                x: 1,
                y: -1
              },
              {
                x: 2,
                y: -4
              }
            ]
          }
        ]
      },
      chartOptions: {
        responsive: true,
        maintainAspectRatio: false,
        onClick: (e) => {
            const canvasPosition = ChartJS.helpers.getRelativePosition(e, chart);

            // Substitute the appropriate scale IDs
            const dataX = chart.scales.x.getValueForPixel(canvasPosition.x);
            const dataY = chart.scales.y.getValueForPixel(canvasPosition.y);
            console.log('Haaa')
        }
      }
      }
    },
  methods: 
  {
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
            ).then(response => {
                this.tables1 = response.data.tables
                this.from = response.data.from
                this.into = response.data.into
                this.join = response.data.join
               console.log(this.join)
            });
        },
      handleFileUpload(){
        this.file = this.$refs.file.files[0];
      }
    }
}
</script>

<style>
.filearea {
  background-image: linear-gradient(
    to right,
    #49005c,
    #0f0061 50%,
    rgb(255, 255, 255) 50%
  );
  background-size: 200% 100%;
  background-position: -100%;
  display: inline-block;
  padding: 5px 0;
  position: relative;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  transition: all 0.3s ease-in-out;
}

.filearea:before{
  content: '';
  background: #22033f;
  display: block;
  position: absolute;
  bottom: -3px;
  left: 0;
  width: 0;
  height: 3px;
  transition: all 0.3s ease-in-out;
}

.filearea:hover {
 background-position: 0;
}

.filearea:hover::before{
  width: 100%;
}
.filearea {
  display: grid;
  font-family: 'Poppins', sans-serif;
  font-size: 27px;
  font-weight: 700;
  place-items: center;
}

</style>
