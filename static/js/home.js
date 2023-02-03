export default {
    data() {
        return {
            all_animals: null,
            home_url: '/api/v1/animals/',
        }
    },
    async mounted() {
        const requestOptions = {
            method: "GET",
        }
        const response = await fetch(this.home_url, requestOptions)
        this.all_animals = await response.json() 
    },
    template: `
    <div v-for="animal in all_animals" :key="animal.id" class="card col-md-6 col-xl-3">
        <img :src="animal.avatar" class="card-img-top" alt="Фото животного">
        <div class="card-body text-center">
            <h5 class="card-title"><span class="badge bg-info">{{ animal.status }}</span>{{ animal.city }}</h5>
            <p class="card-text">{{ animal.name }}
            <span v-if="animal.status === 'on_sale'">{{ animal.price }}</span>
            
            
            </p>
        </div>
    </div>
    
    `
    
}