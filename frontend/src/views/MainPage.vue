<template>
<div><Navbar></Navbar>
   <div class="bg-gradient-to-r from-cyan-500 to-pink-500">
   <div class="px-64">
    <div class="w-full h-screen bg-opacity-25 backdrop-blur bg-white/30 rounded drop-shadow-lg ">
      <div class="flex justify-center">
        <span class="py-8 flex text-3xl font-bsold text-gray-100 hover:text-pink-300">
          Рассматриваемый файл:
        </span>
      </div>
      <div class="grid grid-cols-3">
        <div class="max-w-sm w-full lg:max-w-full lg:flex">
           <div class="h-48 lg:h-auto lg:w-12 flex-none bg-cover rounded-t lg:rounded-t-none lg:rounded-l text-center overflow-hidden">
           </div>
           <div class="border-r border-b border-l border-gray-400 lg:border-l-0 lg:border-t lg:border-gray-400 bg-white rounded-b lg:rounded-b-none lg:rounded-r p-4 flex flex-col justify-between leading-normal">
              <div class="mb-8">
                 <div iv class="text-gray-900 font-bold text-xl mb-2">Функция ебать 1</div>
                 <p class="text-gray-700 text-base">Жора будет всегда сытым</p>
              </div>
           </div>
        </div>
        <div class="max-w-sm w-full lg:max-w-full lg:flex">
          <div class="h-48 lg:h-auto lg:w-12 flex-none bg-cover rounded-t lg:rounded-t-none lg:rounded-l text-center overflow-hidden" >
          </div>
          <div class="border-r border-b border-l border-gray-400 lg:border-l-0 lg:border-t lg:border-gray-400 bg-white rounded-b lg:rounded-b-none lg:rounded-r p-4 flex flex-col justify-between leading-normal">
             <div class="mb-8">
                
                   
                <div iv class="text-gray-900 font-bold text-xl mb-2">Функция ебать 2</div>
                <p class="text-gray-700 text-base">Захар перестанет быть куколдом</p>
             </div>
          </div>
       </div>
       <div class="max-w-sm w-full lg:max-w-full lg:flex">
        <div class="h-48 lg:h-auto lg:w-12 flex-none bg-cover rounded-t lg:rounded-t-none lg:rounded-l text-center overflow-hidden">
        </div>
        <div class="border-r border-b border-l border-gray-400 lg:border-l-0 lg:border-t lg:border-gray-400 bg-white rounded-b lg:rounded-b-none lg:rounded-r p-4 flex flex-col justify-between leading-normal">
           <div class="mb-8">
            
              <div iv class="text-gray-900 font-bold text-xl mb-2">Функция ебать 3</div>
              <p class="text-gray-700 text-base">Игорь найдет девушку выше 170см</p>
           </div>
        </div>
     </div>
     </div>
     <div class="grid grid-cols-1">
      <!-- Snippet -->
<div class="flex flex-col justify-center antialiased text-gray-600 min-h-screen h-screen">
    <div class="max-w-3xl mx-auto p-4 sm:px-6 h-full">
        <!-- Chart widget -->
        <div class="flex flex-col col-span-full xl:col-span-8 bg-white shadow-lg rounded-sm border border-gray-200">
            <header class="px-5 py-4 border-b border-gray-100 flex items-center">
                <h2 class="font-semibold text-gray-800">Общее описание логов</h2>
            </header>
            <div class="px-1 py-1">
                <div class="flex flex-wrap">
                    <!-- Unique Visitors -->
                    <div class="flex items-center py-2">
                        <div class="mr-1">
                            <div class="flex items-center">
                                <div class="text-3xl font-bold text-gray-800 mr-2">24.7K</div>
                            </div>
                            <div class="text-sm text-gray-500">Количество запросов к таблицам</div>
                        </div>
                        <div class="hidden md:block w-px h-8 bg-gray-200 mr-5" aria-hidden="true"></div>
                    </div>
                    <!-- Total Pageviews -->
                    <div class="flex items-center py-2">
                        <div class="mr-1">
                            <div class="flex items-center">
                                <div class="text-3xl font-bold text-gray-800 mr-2">56.9K</div>
                            </div>
                            <div class="text-sm text-gray-500">Количество запросов разработчиков</div>
                        </div>
                        <div class="hidden md:block w-px h-8 bg-gray-200 mr-5" aria-hidden="true"></div>
                    </div>
                    <!-- Bounce Rate -->
                    <div class="flex items-center py-2">
                        <div class="mr-5">
                            <div class="flex items-center">
                                <div class="text-3xl font-bold text-gray-800 mr-2">54K</div>
                                <div class="text-sm font-medium text-yellow-500"></div>
                            </div>
                            <div class="text-sm text-gray-500">Количество запросов загрузчиков</div>
                        </div>
                        <div class="hidden md:block w-px h-8 bg-gray-200 mr-5" aria-hidden="true"></div>
                    </div>
                </div>
            </div>
            <!-- Chart built with Chart.js 3 -->
            <div class="flex">
               <ScatterChart></ScatterChart>
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

</style>
