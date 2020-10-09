<script lang="ts">
    export let currentEnemy:number;
    export let currentSpell:number;
    export let currentColor:number;
    export let length:number = 0;
    export let playSound:Function;

    function changeEnemy():void {
        currentEnemy++;
        if(currentEnemy%length === 4) {
            playSound('tuturu');
        }
    }
</script>

<div class="player-container">
    <h1>Altes Besta</h1>
    <p>Current Enemy: {currentEnemy}</p>
    <button on:click={changeEnemy}>Next Enemy</button>

    <p>Current Spell: {currentSpell}</p>
    <button on:click={() => currentSpell++}>Next Spell</button>
</div>

<style lang="scss">
    .player-container{
        background-color: #303030;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 20px;
        flex: 1 1 auto;
    }
</style>