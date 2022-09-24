<template>
<div><Navbar></Navbar>
   <div class="bg-gradient-to-r from-cyan-500 to-pink-500">
   <div class="px-64">
    <div class="w-full h-screen bg-opacity-25 backdrop-blur bg-white/30 rounded shadow-2xl">
      <div class="flex justify-center filearea">
        <span class="py-8 flex text-4xl font-bold font-corme">
          Рассматриваемый файл:
        </span>
      </div>
      <div class="grid grid-cols-3 col-auto mr-12">
        <div class="max-w-sm w-full lg:max-w-full lg:flex">
           <div class="h-48 lg:h-auto lg:w-12 flex-none bg-cover rounded-t lg:rounded-t-none lg:rounded-l text-center overflow-hidden">
           </div>
           <div class="border-r border-b border-l w-full shadow-xl border-gray-400 lg:border-l-0 lg:border-t lg:border-gray-400 bg-white rounded-b lg:rounded-b-none lg:rounded-r p-4 flex flex-col justify-between leading-normal">
              <div class="mb-8">
                 <div iv class="text-gray-900 font-bold text-3xl mb-2 font-corme text-center">Подсчет запросов к таблицам</div>
                 <p class="text-gray-700 text-xl font-rale text-center">Позволяет проанализировать общее количество запросов к таблице.</p>
              </div>
           </div>
        </div>
        <div class="max-w-sm w-full lg:max-w-full lg:flex">
          <div class="h-48 lg:h-auto lg:w-12 flex-none bg-cover rounded-t lg:rounded-t-none lg:rounded-l text-center overflow-hidden" >
          </div>
          <div class="border-r border-b border-l w-full shadow-xl border-gray-400 lg:border-l-0 lg:border-t lg:border-gray-400 bg-white rounded-b lg:rounded-b-none lg:rounded-r p-4 flex flex-col justify-between leading-normal">
             <div class="mb-8">
                <div iv class="text-gray-900 font-bold text-3xl mb-2 font-corme text-center">Подсчет по запросам от разработчиков</div>
                <p class="text-gray-700 text-xl font-rale text-center">Позволяет выявить наиболее активных разработчиков, и тех кто единожды загрузил данные</p>
             </div>
          </div>
       </div>
       <div class="max-w-sm w-full lg:max-w-full lg:flex">
        <div class="h-48 lg:h-auto lg:w-12 flex-none bg-cover rounded-t lg:rounded-t-none lg:rounded-l text-center overflow-hidden">
        </div>
        <div class="border-r border-b border-l w-full shadow-xl border-gray-400 lg:border-l-0 lg:border-t lg:border-gray-400 bg-white rounded-b lg:rounded-b-none lg:rounded-r p-4 flex flex-col justify-between leading-normal">
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
               <ScatterChart></ScatterChart>
                <div class="container">
                    <div class ="flex justify-center mt-32">
                        <p class="font-semibold text-xl font-corme tracking-widest">Самая используемая таблица</p>
                    </div>
                    <div class="flex justify-center">
                        <p class="font-semibold text-6xl font-rale tracking-widest">2048 записей</p>
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
import Navbar from '../components/Navbar.vue';
import BarChart from '../components/charts/BarChart.vue';

import ScatterChart from '../components/charts/ScatterChart.vue';



export default {
components: { Navbar, BarChart, ScatterChart, BarChart, ScatterChart }
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
