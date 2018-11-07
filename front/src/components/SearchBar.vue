<template>
    <b-container class="search_bar">
        <b-row class="justify-content-md-center">
            <b-col cols="6" align="Center">
                <div class="input-group mb-3">
                    <input v-model="show_searched"
                           v-on:keyup.enter="show_results(show_searched)"
                           v-on:click="clean_message"
                           type="text"
                           class="form-control"
                           aria-label="Serie's name"
                           aria-describedby="button-addon2">
                    <div class="input-group-append">
                        <button class="btn btn-outline-secondary" type="button" id="button-addon2"
                                v-on:click="show_results(show_searched)">Recherche
                        </button>
                    </div>
                </div>
            </b-col>
        </b-row>
        <div class="row justify-content-md-center">
            <ShowCard class="showcard_class"
                v-for="(show, index) in show_list"
                :key="index"
                :title="show.title"
                :overview="show.overview"
                :pict="show.pict"
                :date_next_ep="show.date_next_episode"
                :show_id="show.api_id"
            >
            </ShowCard>
        </div>
    </b-container>
</template>

<script>
    import Episode from "./Episode.vue";
    import ShowCard from "./ShowCard.vue";
    import axios from 'axios';

    export default {
        name: "SearchBar",
        components: {
            Episode,
            ShowCard
        },
        data() {
            // let show_list = [];
            return {
                show_searched: "Game of Thrones...",
                show_list: Array

                // title: "Got",
                // overview: "Le Lorem Ipsum est simplement du faux texte employé dans la composition et la mise en page avant impression. Le Lorem Ipsum est le faux texte standard de l'imprimerie depuis les années 1500, quand un imprimeur anonyme assembla ensemble des morceaux de texte pour réaliser un livre spécimen de polices de texte. Il n'a pas fait que survivre cinq siècles, mais s'est aussi adapté à la bureautique informatique, sans que son contenu n'en soit modifié. Il a été popularisé dans les années 1960 grâce à la vente de feuilles Letraset contenant des passages du Lorem Ipsum, et, plus récemment, par son inclusion dans des applications de mise en page de texte, comme Aldus PageMaker.",
                // pict: "https://www.wikichat.fr/wp-content/uploads/sites/2/Fotolia_99751581_S.jpg",
                // date_next_ep: new Date(),
                // show_id: 1295
            }
        },
        methods: {
            // show_results(show_searched) {
            //     console.log("coucou");
            //     this.show_list = this.show_results_axios(show_searched);
            //     console.log("coucou3");
            // },
            show_results: function (show_searched) {
                axios
                    .get('http://localhost:5000/show/search', {params:{q: show_searched}})
                    .then((response)=>{
                        console.log(response);
                        console.log(response.data);
                        this.show_list = response.data;
                    })
                    .catch((err) => console.log(err))
            },
            clean_message: function () {
                this.show_searched = ""
            }
        }
    }
</script>

<style scoped>
    .search_bar {
        padding: 2px 2px 2px 2px;
    }
    .showcard_class {
        margin: 5px 5px 5px 5px;
    }
</style>