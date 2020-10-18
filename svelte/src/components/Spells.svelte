<script lang="ts">
    import { DialogOverlay, DialogContent } from 'svelte-accessible-dialog';
    import axios from 'axios';
    import { url } from '../utils/server';
    import type { SpellModel, ColorModel } from "../utils/models";

    let spells:SpellModel[] = [];
    let curr:SpellModel = null;
    let newSpell:SpellModel = null;
    let colors:ColorModel[] = [];
    
    function resetSpell() {
        newSpell = {name: '', damage: 0, colors: []};
    }

    resetSpell();

    let files:FileList = null;
    let add=false;

    getSpells();

    function getSpells() {
        axios.get(url + 'spell/').then(result => {
            spells = result.data;
            console.log(spells)
        });
    }

    getColors();

    function getColors() {
        axios.get(url + 'color/').then(result => {
            colors = result.data;
        });
    }

    function handleAdd(evt) {
        evt.preventDefault();
        const data = new FormData();
        for(const key in newSpell) {
            data.append(key, newSpell[key]);
        }
        if(files != null) {
            data.append('image', files[0]);
        }
        const headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        axios.post(url + 'spell/', data, { headers }).then(r => {
            add=false;
            files = null;
            resetSpell();
            getSpells();
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
        if(files) {
            data.append('image', files[0]);
        }
        const headers = {
            'accept': 'application/json',
            'Content-Type': 'multipart/form-data',
        }
        axios.put(url + 'spell/' + curr.id + '/', data, { headers }).then(r => {
            curr=null;
            getSpells();
        }).catch(e => {
            alert('put error');
        });
    }

    function deleteSpell(evt, id) {
        evt.stopPropagation();
        let r = confirm("Delete?");
        if (r) {
            axios.delete(url + 'spell/' + id).then(r => {
                getSpells();
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

            <label for="damage">Damage:</label>
            <input bind:value={curr.damage} type="number" class="input-form" name="damage" required/>

            <label for="image">Image:</label>
            <input bind:files type="file" class="input-form" name="image"/>

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
            <input bind:value={newSpell.name} type="text" class="input-form" name="name" required/>

            <label for="damage">Damage:</label>
            <input bind:value={newSpell.damage} type="number" class="input-form" name="damage" required/>

            <label for="image">Image:</label>
            <input bind:files type="file" class="input-form" name="image" required/>

            <div class="colors">
                {#each colors as color}
                    <div class="color" class:active={newSpell.colors.includes(color)} style="background-color: {color.hexa};" on:click={() => {
                        console.log(newSpell)
                        if(newSpell.colors.includes(color)){
                            newSpell.colors.splice(newSpell.colors.indexOf(color), 1);
                        } else {
                            newSpell.colors.push(color);
                        }
                    }}/>
                {/each}
            </div>

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
        {#each spells as spell}
            <div class="enemy grid-item" on:click={() => curr = spell}>
                <i class="material-icons" on:click={evt => deleteSpell(evt, spell.id)}>delete</i>
                <img src={spell.image} alt="enemy" class="enemy-image" />
                <p class="label">Name</p>
                <p class="enemy-name">{spell.name}</p>
                <p class="label">Damage</p>
                <p class="enemy-name">{spell.damage}</p>
                <div class="colors">
                    {#each spell.colors as color}
                        <div class="color" style="background-color: {color.hexa};" />
                    {/each}
                </div>
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
    }

    .colors{
        display: flex;

        .color{
            width: 20px;
            height: 20px;
            border-radius: 50%;
            margin: 5px;
            cursor: pointer;
        }
        .active{
            box-shadow: 0px 0px 10px #FFF;
        }
    }
</style>