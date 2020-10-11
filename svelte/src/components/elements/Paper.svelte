<script lang="ts">
    import { onMount } from 'svelte';
    import paper from 'paper';
    import type { PlayerModel, SpellModel } from '../../utils/models';

    export let currentColor:number;
    export let currentSpell:number;
    export let colors:string[];
    export let spells:SpellModel[];
    let spellCooldown:number = 250;
    export let submitSpell:Function;
    export let player:PlayerModel;
    export let special:Function;
    export let restartGame:Function;
    export let changing:boolean;
    export let started:boolean;
    export let lost:boolean;

    onMount(():void => {
        paper.setup("paper");

        let myPath:any;
        let disable:boolean = false;
        let wasDisabled: boolean = false;

        paper.view.onMouseDown = function(event:any):void {
            wasDisabled = disable;
        	if (rMousePress) {
                myPath.remove();
            } else {
                if (!disable && !changing){
                    myPath = new paper.Path({
                        strokeColor: colors[currentColor%colors.length],
                        strokeWidth: 20,
                        strokeCap: 'round'
                    });
                    myPath.smooth({ type: 'continuous' });
                }
            }
        }
        
        paper.view.onMouseDrag = function(event:any):void {
            if (!disable) {
                myPath.add(event.point);
            }
        }

        paper.view.onMouseUp = function(event:any):void {
            if(!wasDisabled) {
                disable = true;
                var canvas = document.getElementById("paper")
                var img = canvas.toDataURL();
                submitSpell(img);

                setTimeout(() => {
                    paper.project.activeLayer.removeChildren();
                    disable = false;    
                    currentSpell++;
                }, spellCooldown);
            }
        }

        paper.view.draw();
    });

    export let rMousePress:boolean;

</script>

<div class="paper-container">
    <div class="preview-container">
        <div class="spell-container">
            <span>Next Spell:</span>
            <img class="spell" src={spells[(currentSpell+1)%spells.length].image} alt="next-spell" />
        </div>
        <div class="spell-container">
            <span>Current Spell:</span>
            <img class="current-spell" src={spells[currentSpell%spells.length].image} alt="spell" />
        </div>
        <div class="right-div">
            <div class="colors">
                {#each colors as color, i}
                    <div class="color" class:active={currentColor === Number(i)} style="background-color: {color};" on:click={() => currentColor = Number(i)}/>
                {/each}
            </div>
            <div class="wrap">
                {#if player.currentMana === player.mana}
                    <button class="button" on:click={special}>Special</button>
                {/if}
            </div>
        </div>
    </div>
    <div class="canvas-container">
        {#if !started}
            <div class="wrap">
                {#if lost}
                    <h1>Game Over</h1>
                {/if}
                <button class="button" on:click={() => {started=true; restartGame()}}>Start Game</button>        
            </div>
        {/if}
        <canvas id="paper"/>
    </div>
</div>

<style type="text/scss">
    .paper-container{
        display: flex;
        flex-direction: column;
        flex: 3 1 auto;
        margin: 0 15px;
        height: 100%;
    }
    .preview-container{
        background-color: #303030;
        padding: 20px;
        margin-bottom: 15px;
        flex: 1;
        display: grid;
        grid-template-columns: repeat(3, 1fr); 
        grid-column-gap: var(--spacing-l);
        grid-row-gap: var(--spacing-l);
        width: 100%;
        align-items: flex-start;

        .spell-container{
            display: flex;
            flex-direction: column;
            height: 100%;
            align-items: center;
        }

        .spell{
            max-height: 100px;
            margin: auto;
        }

        .current-spell{
            max-height: 250px;
            margin: auto;
        }
    }
    .canvas-container{
        padding: 20px;
        background-color: #303030;
        flex: 3;
        min-height: 0; /* new */

        #paper{
            width: 100%;
            height: 100%;
        }
    }

    .right-div{
        position: relative;
        height: 100%;

        .colors{
            position: absolute;
            display: flex;
            justify-content: flex-end;
            right: 0;

            .color{
                width: 20px;
                height: 20px;
                border-radius: 50%;
                margin: 5px;
            }
            .active{
                box-shadow: 0px 0px 10px #FFF;
            }
        }
    }

    .wrap {
        height: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }

    .button {
        min-width: 200px;
        min-height: 50px;
        font-family: 'Nunito', sans-serif;
        font-size: 22px;
        text-transform: uppercase;
        letter-spacing: 1.3px;
        font-weight: 700;
        color: #303030;
        background: linear-gradient(90deg, orangered 0%, red 100%);
        border: none;
        border-radius: 1000px;
        transition: all 0.3s ease-in-out 0s;
        cursor: pointer;
        outline: none;
        position: relative;
        padding: 10px;
    }

    button::before {
        content: '';
        border-radius: 1000px;
        min-width: calc(200px + 12px);
        min-height: calc(50px + 12px);
        border: 6px solid orangered;
        box-shadow: 0 0 60px rgba(orangered,.64);
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        opacity: 0;
        transition: all .3s ease-in-out 0s;
    }

    .button:hover, .button:focus {
        color: #313133;
        transform: translateY(-6px);
    }

    button:hover::before, button:focus::before {
        opacity: 1;
    }

    button:hover::after, button:focus::after {
        animation: none;
        display: none;
    }

    @keyframes ring {
        0% {
            width: 30px;
            height: 30px;
            opacity: 1;
        }
        100% {
            width: 300px;
            height: 300px;
            opacity: 0;
        }
    }

</style>