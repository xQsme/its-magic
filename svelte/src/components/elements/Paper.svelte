<script lang="ts">
    import { onMount } from 'svelte';
    import paper from 'paper';

    export let currentColor:string;
    let spellCooldown:number = 250; //250


    onMount(():void => {
        //paper.install(window);
        paper.setup("paper");
        //draw();

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
                        strokeColor: currentColor,
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

    // function draw() {
    //     const path = new paper.Path.Circle({
    //         center: [80, 50],
    //         radius: 35,
    //         fillColor: "red",
    //     });

    //     const secondPath = new paper.Path.Circle({
    //         center: [120, 50],
    //         radius: 35,
    //         fillColor: "#00FF00",
    //     });
    // }

    export let showPaper:boolean;
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

<canvas id="paper" class:show-paper={showPaper} on:mousedown={startDrawing} on:mousemove={keepDrawing} on:mouseup={finishDrawing} /> 

<style type="text/scss">
    #paper{
        width: 100%;
        height: 100%;
        background: transparent;
        position: fixed;
        visibility: hidden;
        /* background-color: white;
        width: 50%;
        height: 50%;
        transform: translate(50%, 50%); */
    }
    .show-paper{
        visibility: visible !important;
    }
</style>