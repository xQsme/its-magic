<script lang="ts">
    import { onMount, onDestroy, beforeUpdate } from 'svelte';
    import type { EnemyModel } from '../../utils/models';
    
    export let enemy:EnemyModel;
    export let dealDamageToPlayer:Function;
    let interval;
    export let started:boolean;
    export let damage:any[];

    onMount(():void => {
        interval = setInterval(enemyMana, 200);
    });

    function enemyMana(){
        if(started) {
            enemy.currentMana++;
            if(enemy.currentMana >= enemy.mana) {
                enemy.currentMana = 0;
                dealDamageToPlayer();
            }
        }
    }

    function spellActivation(){
        console.log("hihihisahdiashidoahsid")
    }

    onDestroy(():void => {
        clearInterval(interval);
    });

    beforeUpdate(() => {
		damage=damage;
	});

</script>

<div class="container">
    <h1>{enemy.name}</h1>
    <div class="stats">
        <div class="health">
            <span>HP: {enemy.currentHP}/{enemy.hp}</span>
            <div class="progress-container">
                <div class="progress-placeholder" />
                <div class="progress" style="width: {enemy.currentHP/enemy.hp*100}%;" />
                <span class="progress-text">{(enemy.currentHP/enemy.hp*100).toFixed(2)}%</span>
            </div>
        </div>
        <div class="mana">
            <span>MP: {enemy.currentMana}/{enemy.mana}</span>
            <div class="progress-container">
                <div class="progress-placeholder" />
                <div class="progress" style="width: {enemy.currentMana/enemy.mana*100}%;" />
                <span class="progress-text">{(enemy.currentMana/enemy.mana*100).toFixed(2)}%</span>
            </div>
        </div>
    </div>
    <div class="enemy-container">
        {#each damage as d (d.random)}
            <span class="damage" style="margin-right: {d.random}%">{d.value}</span>
        {/each}
        <img class="enemy" src={enemy.image} alt="enemy"/>
    </div> 
</div>

<style lang="scss">
    .damage {
        font: bold 1.7em 'Times Roman';
        position: absolute;
        animation: 2s;
        animation-fill-mode: forwards;
        animation-name: slideup;
        right: 0;
    }
    
    @keyframes slideup {
        0% {
            top: 50%;
            color: white;
        }

        100% {
            top: 20px;
            color: #ff392e;
        }  
    }    

    .container{
        position: relative;
        display: flex;
        background-color: #303030;
        flex-direction: column;
        flex: 1 1 auto;
        padding: 20px;

        h1{
            text-align: center;
            margin: 0;
        }

        .health{
            color: #ff392e;
            margin-bottom: 10px;

            .progress{
                background-color: #ff392e;
            }
        }

        .mana{
            color: cornflowerblue;

            .progress{
                background-color: cornflowerblue;
            }
        }

        .progress-container{
            width: 100%;
            height: 20px;
            position: relative;

            .progress{
                height: 100%;
                border-radius: 10px;
                transition: width 0.5s;
            }

            .progress-text{
                color: white;
                position: absolute;
                top: 0;
                right: 50%;
                transform: translate(50%);
            }

            .progress-placeholder{
                height: 100%;
                width: 100%;
                border-radius: 10px;
                background-color: #222222;
                margin-bottom: -20px;
            }
        }

        .enemy-container{
            position: relative;
            display: flex;
            justify-content: center;
            align-items: center;      
            height: 100%;  

            .enemy{
                max-width: 20vw;
            }
        }
    }


    

</style>