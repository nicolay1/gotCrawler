<template>
    <div class="container">
        <div>
            <SearchBar/>
        </div>
    </div>


</template>
<script>
    import ActorList from "./components/ActorList.vue";
    import AuthorList from "./components/AuthorList.vue";
    import SearchBar from "./components/SearchBar.vue";
    export default {
        name: 'App',
        components: {
            ActorList,
            AuthorList,
            SearchBar
        },
        data() {
            return {}
        }
    }
</script>
