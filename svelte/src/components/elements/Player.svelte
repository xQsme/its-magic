<script lang="ts">
    import type { PlayerModel } from "../../utils/models";
    import { beforeUpdate } from 'svelte';
    export let player:PlayerModel;
    export let damage:any[];
    export let xp:any[];
    export let levelUp:boolean;

    beforeUpdate(() => {
        damage=damage;
        xp=xp;
        levelUp=levelUp;
	});
</script>

        <div class="gradient"></div>
<div class="player-container">
    <h1>{player.name}</h1>
    <div class="stats">
        <div class="health">
            <span>HP: {player.currentHP}/{player.hp}</span>
            <div class="progress-container">
                <div class="progress-placeholder" />
                <div class="progress" style="width: {player.currentHP/player.hp*100}%;" />
                <span class="progress-text">{(player.currentHP/player.hp*100).toFixed(2)}%</span>
            </div>
        </div>
        <div class="mana">
            <span>MP: {player.currentMana}/{player.mana}</span>
            <div class="progress-container">
                <div class="progress-placeholder" />
                <div class="progress" style="width: {player.currentMana/player.mana*100}%;" />
                <span class="progress-text">{(player.currentMana/player.mana*100).toFixed(2)}%</span>
            </div>
        </div>
        <div class="xp">
            <span>XP: {player.currentXP}/{player.xp}</span>
            <div class="progress-container">
                <div class="progress-placeholder" />
                <div class="progress" style="width: {player.currentXP/player.xp*100}%;" />
                <span class="progress-text">{(player.currentXP/player.xp*100).toFixed(2)}%</span>
            </div>
        </div>
    </div>
    <div class="image-container">
        {#each damage as d (d.random)}
            <span class="damage" style="margin-right: {d.random}%">{d.value}</span>
        {/each}
        {#each xp as x (x.random)}
            <span class="xp-float" style="margin-right: {x.random}%">{x.value}</span>
        {/each}
        {#if levelUp}
            <h1 class="level">LEVEL UP!</h1>
        {/if}
        <img class="player" src={player.image} alt="besta"/>
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

    .xp-float {
        font: bold 1.7em 'Times Roman';
        position: absolute;
        animation: 3.5s;
        animation-fill-mode: forwards;
        animation-name: slidexp;
        right: 0;
    }
    
    @keyframes slidexp {
        0% {
            top: 50%;
            color: white;
        }

        100% {
            top: 20px;
            color: #fdfd96;
        }  
    }

    .level{
        position: absolute;
        color:  #fdfd96;
        top: 20px;

        font: 600 2.5em/1 "Oswald", sans-serif;
        letter-spacing: 0;
        padding: .25em 0 .325em;
        display: block;
        margin: 0 auto;

    /* Clip Background Image */

        background: url('../assets/images/gradient.png') repeat-y;
        -webkit-background-clip: text;
        background-clip: text;

    /* Animate Background Image */

        -webkit-text-fill-color: transparent;
        -webkit-animation: aitf 10s linear infinite;

    /* Activate hardware acceleration for smoother animations */

        -webkit-transform: translate3d(0,0,0);
        -webkit-backface-visibility: hidden;

    }

    /* Animate Background Image */

    @-webkit-keyframes aitf {
        0% { 
            background-position: 0% 50%;
        }
        100% { 
            background-position: 100% 50%;
         }
    }    

    .player-container{
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
            margin-bottom: 10px;

            .progress{
                background-color: cornflowerblue;
            }
        }

        .xp{
            color: #fdfd96;
            margin-bottom: 10px;

            .progress{
                background-color: #fdfd96;
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

        .image-container{
            position: relative;
            display: flex;
            justify-content: center;
            align-items: center;      
            height: 100%;  
            
            .player{
                max-width: 20vw;
            }
        }
    }
</style>