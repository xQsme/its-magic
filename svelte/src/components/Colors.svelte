<script lang="ts">
    import { DialogOverlay, DialogContent } from 'svelte-accessible-dialog';
    import axios from 'axios';
    import { url } from '../utils/server';
    import type { ColorModel } from "../utils/models";

    let colors:ColorModel[] = [];
    let curr:ColorModel = null;
    let newColor:ColorModel = null;
    
    function resetColor() {
        newColor = {name: '', hexa: ''};
    }

    resetColor();

    let add=false;

    getColors();

    function getColors() {
        axios.get(url + 'color/').then(result => {
            colors = result.data;
        });
    }

    function handleAdd(evt) {
        evt.preventDefault();
        const data = new FormData();
        for(const key in newColor) {
            data.append(key, newColor[key]);
        }
        axios.post(url + 'color/', data).then(r => {
            add=false;
            resetColor();
            getColors();
        }).catch(e => {
            alert('post error');
        });
    }

    function handleEdit(evt) {
        evt.preventDefault();
        const data = new FormData();
        for(const key in curr) {
            if(key !== 'image') {
                data.append(key, curr[key]);
            }
        }
        axios.put(url + 'color/' + curr.id + '/', data).then(r => {
            curr=null;
            getColors();
        }).catch(e => {
            alert('put error');
        });
    }

    function deleteSpell(evt, id) {
        evt.stopPropagation();
        let r = confirm("Delete?");
        if (r) {
            axios.delete(url + 'color/' + id).then(r => {
                getColors();
            }).catch(e => {
                alert('delete error');
            })
        }
    }
</script>

<DialogOverlay isOpen={curr !== null} onDismiss={() => curr = null}>
    <DialogContent class="dialog" aria-label="Announcement">
        <form class="dialog-container" on:submit={handleEdit}>
            <label for="name">Name:</label>
            <input bind:value={curr.name} type="text" class="input-form" name="name" required/>

            <label for="hexa">Color:</label>
            <input bind:value={curr.hexa} type="text" class="input-form" name="hexa" required/>

            <div class="dialog-buttons">
                <button>Submit</button>
                <button on:click={() => curr = null}>Close</button>
            </div>
        </form>
    </DialogContent>
</DialogOverlay>

<DialogOverlay isOpen={add} onDismiss={() => add = false}>
    <DialogContent class="dialog" aria-label="Announcement">
        <form class="dialog-container" on:submit={handleAdd}>
            <label for="name">Name:</label>
            <input bind:value={newColor.name} type="text" class="input-form" name="name" required/>

            <label for="hexa">Color:</label>
            <input bind:value={newColor.hexa} type="text" class="input-form" name="hexa" required/>

            <div class="dialog-buttons">
                <button>Submit</button>
                <button on:click={() => add = false}>Close</button>
            </div>
        </form>
    </DialogContent>
</DialogOverlay>

<div class="enemies-container">
    <div class="grid-container">
        <div class="add grid-item" on:click={() => add = true}>
            <i class="material-icons">add_circle</i>
        </div>
        {#each colors as color}
            <div class="enemy grid-item" on:click={() => curr = color}>
                <i class="material-icons" on:click={evt => deleteSpell(evt, color.id)}>delete</i>
                <div class="color-container">
                    <div class="color" style="background-color: {color.hexa}"/>
                </div>
                <p class="label">Name</p>
                <p class="enemy-name">{color.name}</p>
                <p class="label">Hex</p>
                <p class="enemy-name">{color.hexa}</p>
            </div>
        {/each}
    </div>
</div>

<style lang="scss">
    .dialog-container{
        display: flex;
        flex-direction: column;

        .dialog-buttons{
            display: flex;
            justify-content: space-between;
            margin-top: 20px;
        }
    }

    .enemies-container{
        width: 100%;
        overflow: auto;
    }

    .grid-container{
        max-width: 1200px;
        display: grid;
        grid-auto-rows: 1fr;
        grid-template-columns: repeat(4, 1fr); 
        grid-column-gap: 20px;
        grid-row-gap: 20px;
        width: 100%;
        padding: 20px;
        margin: auto;

        .enemy{

            i{
                text-align: right;
                margin-bottom: 10px;
                transition: color .2s linear;
            }

            i:hover{
                color: orangered;
            }

            p{
                margin: 0;
            }

            .label{
                opacity: 0.5;
                font-size: 14px;
                margin-top: 5px;
            }

            .enemy-image{
                max-width: 100%;
            }
        }

        .add{
            justify-content: center;
            align-items: center;

            i{
                font-size: 120px;
                transition: color .2s linear;
            }
        }

        .grid-item{
            display: flex;
            flex-direction: column;
            background-color: #303030;
            padding: 20px;
            cursor: pointer;
            transition: transform .2s, border-radius .2s;
        }

        .add:hover{
            i{
                color: orangered;
            }
        }

        .grid-item:hover{
            transform: scale(1.05);
            border-radius: 10px;
        }

        .color{
            width: 100%;
            border-radius: 50%;
            padding-top: 100%;
        }
    }
</style>