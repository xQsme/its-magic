<script lang="ts">
    export let enemy:Enemy;
</script>

<div class="enemy-container">
    <img src={enemy.image} alt="enemy"/>
</div>

<style lang="scss">
    .enemy-container{
        background-color: #303030;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 20px;
        flex: 1 1 auto;

        img{
            max-width: 100%;
        }
    }
</style>