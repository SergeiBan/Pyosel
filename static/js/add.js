export default {
    data() {
        return {
            welcome: 'Опишите животное',
            city: null,
            parent: null,
            species: null,
            name: null,
            breed: null,
            description: null,
            color: null,
            price: null,
            status: null,
            avatar: null,
            auxPhoto: null,
            avatar_url: null,
            auxPhoto_url: null,
            token: window.localStorage.getItem('token'),
            errors: null
        }
    },
    methods: {
        async add_submit(e) {

            let data = new FormData()
            data.append('city', this.city)
            data.append('species', this.species)
            data.append('name', this.name)
            data.append('status', this.status)
            data.append('avatar', this.avatar)
            data.append('aux_photo', this.auxPhoto)

            const requestOptions = {
                method: "POST",
                headers: {"Authorization": `Token ${this.token}`},
                body: data
            }

            const response = await fetch('/api/v1/animals/', requestOptions)
            const responseJson = await response.json()
            if (response['status'] != 201) {
                this.errors = Object.values(responseJson)
                return
            }
            this.$router.push('/')
            
        },
        add_photos(event) {
            const img_data = event.target.files[0]
            
            const fieldName = event.target.name
            const fieldId = event.target.id
            const img_url = URL.createObjectURL(img_data)

            const imagebox = document.getElementById('image-box')
            const crop_btn = document.getElementById('crop-btn')
            const inputField = document.getElementById(fieldId)

            imagebox.innerHTML = `<img src="${ img_url }" id="image" style="width:100%;"></img>`
            const image = document.getElementById('image')
            
            document.getElementById('image-box').style.display = 'block'
            document.getElementById('crop-btn').style.display = 'block'
            document.getElementById('confirm-btn').style.display = 'none'

            const cropper = new Cropper(image, {
                aspectRatio: 1 / 1,
                autoCropArea: 1,
                viewMode: 1,
                scalable: false,
                zoomable: false,
                movable: false,
                minCropBoxWidth: 200,
                minCropBoxHeight: 200,
            })

            crop_btn.addEventListener('click', ()=>{
                cropper.getCroppedCanvas().toBlob((blob)=>{
                  
                  let file = new File([blob], img_data.name,{type:"image/*", lastModified:new Date().getTime()});
                  let container = new DataTransfer();
                  container.items.add(file);
                  inputField.files = container.files;
        
                  document.getElementById('image-box').style.display = 'none'
                  document.getElementById('crop-btn').style.display = 'none'
                  document.getElementById('confirm-btn').style.display = 'block'

                  const url_cropped = URL.createObjectURL(file)
                  if (fieldName == 'avatar') { this.avatar_url = url_cropped; this.avatar = file }
                  if (fieldName == 'aux_photo') { this.auxPhoto_url = url_cropped; this.auxPhoto = file }
        
                }, img_data.type, 0.7);
            });
        }
    },
    template: `
    <form @submit.prevent="add_submit" enctype="multipart/form-data">
        <p>{{ welcome }}</p>

        <div v-if="errors">
            <div v-for="error in errors" :key="error.id">
                <small v-for="error_part in error" :key="error_part.id" class="text-primary">
                    {{ error_part }}
                </small>
            </div>
        </div>

        <h2>Обязательные поля</h2>

        <input v-model="city" class="form-control mb-2" placeholder="Город" required>

        <select v-model="status" class="form-select mb-2" required>
            <option selected disabled value="">Статус</option>
            <option value="boasting">Просто хвастаюсь</option>
            <option value="free_to_take">В хорошие руки</option>
            <option value="on_sale">Продается</option>
            <option value="lost">Потерялся</option>
            <option value="found">Найден</option>
        </select>

        <input class="form-control mb-2" v-model="price" v-if="status === 'on_sale'" type="number" placeholder="Цена ₽">
        <input v-model="name" class="form-control mb-4" v-if="status !== 'found'" placeholder="Кличка" required>

        <select v-model="species" class="form-select mb-2" required>
            <option disabled value="">Категория</option>
            <option value="dogs">Собаки</option>
            <option value="cats">Кошки</option>
        </select>
        
        

        <h2>Необязательные поля</h2>
        <div class="row">
            <div class="col-md-6">
                <label for="avatar">Главное фото</label>
                <input id="avatar" type="file" accept="image/*" @change="add_photos" class="form-control mb-2" name="avatar">
                <img v-if="avatar_url" :src="avatar_url" alt="Просмотр главного фото" class="img-fluid img-thumbnail">
            </div>
            <div class="col-md-6">
                <label for="auxiliary">Дополнительное фото</label>
                <input id="auxiliary" type="file" accept="image/*" @change="add_photos" class="form-control mb-2" name="aux_photo">
                <img v-if="auxPhoto_url" :src="auxPhoto_url" alt="Предпросмотр дополнительного фото" class="img-fluid img-thumbnail">
            </div>
        </div>

        <div style="position: absolute; top: 15px;">
            <div id="image-box" class="image-container"></div>
            <button class="btn btn-info" id="crop-btn" style="width: 100%; margin-top: 10px; display: none;" type="button">Образать</button>  
        </div>
        
        <button class="btn btn-outline-info" id="confirm-btn" style="width: 100%; margin-top: 10px;" type="submit">Добавить</button>
        <!-- <input type="submit" class="form-control btn btn-outline-info" value="Добавить"> -->
    </form>
    `
}