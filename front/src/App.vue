<template>
    <div class="container">
        <div class="row">
            <ShowCard :title=title :overview=overview :pict=pict :date_next_ep=date_next_ep :show_id="show_id"></ShowCard>
        </div>
    </div>
</template>

<script>
    import ShowCard from './components/ShowCard.vue'

    export default {
        name: 'App',
        components: {
            ShowCard
        },
        data() {
            return {
                title: "Got",
                overview: "Le Lorem Ipsum est simplement du faux texte employé dans la composition et la mise en page avant impression. Le Lorem Ipsum est le faux texte standard de l'imprimerie depuis les années 1500, quand un imprimeur anonyme assembla ensemble des morceaux de texte pour réaliser un livre spécimen de polices de texte. Il n'a pas fait que survivre cinq siècles, mais s'est aussi adapté à la bureautique informatique, sans que son contenu n'en soit modifié. Il a été popularisé dans les années 1960 grâce à la vente de feuilles Letraset contenant des passages du Lorem Ipsum, et, plus récemment, par son inclusion dans des applications de mise en page de texte, comme Aldus PageMaker.",
                pict: "https://www.wikichat.fr/wp-content/uploads/sites/2/Fotolia_99751581_S.jpg",
                date_next_ep: new Date(),
                show_id:1295
            }
        }
    }
</script>