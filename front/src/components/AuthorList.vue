<template>

    <b-container class="author_class" fluid>
        <b-row align-v="center" >
            <Author
                v-for="author in authors"
                v-bind:name_author="author.name_author"
                v-bind:role_author="author.role_author"
            >
            </Author>
        </b-row>
    </b-container>


</template>
<script>
    import Author from "./Author.vue";
    export default {
        name: "AuthorList",
        components: {
            Author,
        },
        props: {
            authors: Array,
        }
    }
</script>
