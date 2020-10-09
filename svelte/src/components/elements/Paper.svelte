<script lang="ts">
    import { onMount } from 'svelte';
    import paper from 'paper';
import type { SpellModel } from '../../utils/models';

    export let currentColor:number;
    export let currentSpell:number;
    export let colors:string[];
    export let spells:SpellModel[];
    let spellCooldown:number = 250;


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
                if (!disable){
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

    let started:boolean = false;

    function startDrawing(evt:any):void{
        started = true;
    }

    function keepDrawing(evt:any):void{
        if(started) {
            //console.log(evt);
        }
        if (rMousePress) {
            started = false;
            rMousePress = false;
        }
    }

    function finishDrawing(evt:any):void{
        started = false;
    }

</script>

<div class="paper-container">
    <div class="preview-container">
        <img class="spell" src={spells[(currentSpell+1)%spells.length].image} alt="next-spell" />
        <img class="current-spell" src={spells[currentSpell%spells.length].image} alt="spell" />
        <div class="colors">
            {#each colors as color, i}
                <div class="color" class:active={currentColor === Number(i)} style="background-color: {color};" on:click={() => currentColor = Number(i)}/>
            {/each}
        </div>
    </div>
    <div class="canvas-container">
        <canvas id="paper" on:mousedown={startDrawing} on:mousemove={keepDrawing} on:mouseup={finishDrawing} />
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
        position: relative;
        background-color: #303030;
        padding: 20px;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        flex: 1;

        .spell{
            max-height: 50px;
        }

        .current-spell{
            max-height: 250px;
        }
    }
    .canvas-container{
        padding: 20px;
        background-color: #303030;
        flex: 2;

        #paper{
            width: 100%;
            height: 100%;
        }
    }
    .colors{
        position: absolute;
        display: flex;
        top: 20px;
        right: 20px;
    }
    .color{
        width: 20px;
        height: 20px;
        border-radius: 50%;
        margin: 5px;
    }
    .active{
        box-shadow: 0px 0px 10px #FFF;
    }
</style>