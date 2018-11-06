<template>
    <div class="container">
        <ActorList
                :actors= actor_list>
        </ActorList>
        <AuthorList
                :authors= author_list>
        </AuthorList>
    </div>
</template>
<script>
    import ActorList from "./components/ActorList.vue";
    import AuthorList from "./components/AuthorList.vue";
    export default {
        name: 'App',
        components: {
            ActorList,
            AuthorList
        },
        data() {
            return {
                actor_list: [
                    {
                        name: "Johnny Depp",
                        pict: "https://img1.closermag.fr/var/closermag/storage/images/bio-people/biographie-johnny-depp-112279/815563-1-fre-FR/Johnny-Depp_square500x500.jpg"
                    },
                    {
                        name: "Leonardo Dicaprio",
                        pict: "https://img3.closermag.fr/var/closermag/storage/images/1/2/5/7/7/12577149/leonardo-dicaprio-beverly-hills-2004_exact1024x768_p.jpg"
                    },
                    {
                        name: "Johnny Depp",
                        pict: "https://img1.closermag.fr/var/closermag/storage/images/bio-people/biographie-johnny-depp-112279/815563-1-fre-FR/Johnny-Depp_square500x500.jpg"
                    },
                    {
                        name: "Leonardo Dicaprio",
                        pict: "https://img3.closermag.fr/var/closermag/storage/images/1/2/5/7/7/12577149/leonardo-dicaprio-beverly-hills-2004_exact1024x768_p.jpg"
                    },
                    {
                        name: "Johnny Depp",
                        pict: "https://img1.closermag.fr/var/closermag/storage/images/bio-people/biographie-johnny-depp-112279/815563-1-fre-FR/Johnny-Depp_square500x500.jpg"
                    },
                    {
                        name: "Leonardo Dicaprio",
                        pict: "https://img3.closermag.fr/var/closermag/storage/images/1/2/5/7/7/12577149/leonardo-dicaprio-beverly-hills-2004_exact1024x768_p.jpg"
                    },
                    {
                        name: "Johnny Depp",
                        pict: "https://img1.closermag.fr/var/closermag/storage/images/bio-people/biographie-johnny-depp-112279/815563-1-fre-FR/Johnny-Depp_square500x500.jpg"
                    },
                    {
                        name: "Leonardo Dicaprio",
                        pict: "https://img3.closermag.fr/var/closermag/storage/images/1/2/5/7/7/12577149/leonardo-dicaprio-beverly-hills-2004_exact1024x768_p.jpg"
                    }
                ],
                author_list: [
                    {
                        name_author: "Spielberg",
                        role_author: "Réalisateur"
                    },
                                        {
                        name_author: "Spielberg avec un nom vraiment très très long",
                        role_author: "Réalisateur"
                    },
                                        {
                        name_author: "Spielberg",
                        role_author: "Réalisateur avec un rôle vraiment très très long"
                    },
                                        {
                        name_author: "Spielberg avec un nom vraiment très très long",
                        role_author: "Réalisateur avec un rôle vraiment très très long"
                    },
                                        {
                        name_author: "Spielberg",
                        role_author: "Réalisateur"
                    },                    {
                        name_author: "Spielberg",
                        role_author: "Réalisateur"
                    },
                                        {
                        name_author: "Spielberg avec un nom vraiment très très long",
                        role_author: "Réalisateur"
                    },
                                        {
                        name_author: "Spielberg",
                        role_author: "Réalisateur avec un rôle vraiment très très long"
                    }
                ]
            }
        }
    }
</script>
