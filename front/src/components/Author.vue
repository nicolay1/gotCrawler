<template>
    <b-col cols="4" align="Center" class="author_card">
        <b-container class="card">
            <b-row align-v="center">
                <b-col md="12" lg="6" align="Center" class="name_author">
                    {{name_author}}
                </b-col>
            </b-row>
            <b-row align-v="center">
                <b-col md="12" lg="6" align="Center" class="role_author">
                    {{role_author}}
                </b-col>
            </b-row>
        </b-container>
    </b-col>
</template>
<script>
    export default {
        name: "Author",
        props: {
            name_author: String,
            role_author: String,
        }
    }
</script>
<style scoped>
    .author_card{
        margin-top: 2px;
        padding: 2px 2px 2px 2px;
    }
    .name_author {
        text-align: center;
    }
    .role_author {
        text-align: center;
        font-style: italic;
    }
</style>