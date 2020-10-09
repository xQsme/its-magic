<script lang="ts">
    import { onMount } from 'svelte';
    import paper from 'paper';

    export let currentColor:string;
    export let colors:string[];
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
    <div class="colors">
        {#each colors as color, i}
            <div class="color" class:active={currentColor === Number(i)} style="background-color: {color};" on:click={() => currentColor = Number(i)}/>
        {/each}
    </div>
    <canvas id="paper" on:mousedown={startDrawing} on:mousemove={keepDrawing} on:mouseup={finishDrawing} />
</div>

<style type="text/scss">
    .paper-container{
        background-color: #303030;
        padding: 20px;
        flex: 3 1 auto;
        margin: 0 15px;
    }
    #paper{
        width: 100%;
        height: 100%;
    }
    .colors{
        display: flex;
        width: 100%;
        justify-content: right;
        align-items: center;
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