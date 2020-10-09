<script lang="ts">
    export let enemy:Enemy;
</script>

<div class="enemy-container">
    <img src="./assets/images/health.png">
    <img src="./assets/images/mana.png">
    <img class="enemy" src={enemy.image} alt="enemy"/>    
</div>

<style lang="scss">
    .enemy-container{
        background-color: #303030;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 20px;
        flex: 1 1 auto;

        .enemy{
            max-width: 100%;
        }
    }

</style>