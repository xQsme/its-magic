<script lang="ts">
    import type { EnemyModel } from '../utils/models';
    import axios from 'axios';
    import { url } from '../utils/server';
    import { DialogOverlay, DialogContent } from 'svelte-accessible-dialog';

    let enemies:EnemyModel[] = [];
    let curr:EnemyModel = null;
    let newEnemy:EnemyModel;

    function resetEnemy() {
        newEnemy = {name: '', xp: 0, hp: 0, mana: 0, damage: 0, currentHP: 0, currentMana: 0};
    }

    resetEnemy();

    let files:FileList = null;
    let sounds:FileList = null;
    let add=false;

    getEnemies();

    function getEnemies() {
        axios.get(url + 'enemy/').then(result => {
            enemies = result.data;
        });
    }

    function handleAdd(evt) {
        evt.preventDefault();
        const data = new FormData();
        for(const key in newEnemy) {
            if(key !== 'sound' && key !== 'image') {
                data.append(key, newEnemy[key]);
            }
        }
        if(files !== null) {
            data.append('image', files[0]);
        }
        if(sounds !== null) {
            data.append('sound', sounds[0]);
        }
        const headers = {
            'Content-Type': 'multipart/form-data',
        }
        axios.post(url + 'enemy/', data, { headers }).then(r => {
            add=false;
            files = null;
            sounds = null;
            resetEnemy();
            getEnemies();
        }).catch(e => {
            alert('post error');
        });
    }

    function handleEdit(evt) {
        evt.preventDefault();
        const data = new FormData();
        for(const key in curr) {
            if(key !== 'sound' && key !== 'image') {
                data.append(key, curr[key]);
            }
        }
        if(files !== null) {
            data.append('image', files[0]);
        }
        if(sounds !== null) {
            data.append('sound', sounds[0]);
        }
        const headers = {
            'accept': 'application/json',
            'Content-Type': 'multipart/form-data',
        }
        axios.put(url + 'enemy/' + curr.id + '/', data, { headers }).then(r => {
            curr=null;
            files = null;
            sounds = null;
            getEnemies();
        }).catch(e => {
            alert('put error');
        });
    }

    function deleteEnemy(evt, id) {
        evt.stopPropagation();
        let r = confirm("Delete?");
        if (r) {
            axios.delete(url + 'enemy/' + id).then(r => {
                getEnemies();
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

            <label for="xp">XP:</label>
            <input bind:value={curr.xp} type="number" class="input-form" name="xp" required/>

            <label for="hp">HP:</label>
            <input bind:value={curr.hp} type="number" class="input-form" name="hp" required/>

            <label for="mana">Mana:</label>
            <input bind:value={curr.mana} type="number" class="input-form" name="mana" required/>

            <label for="damage">Damage:</label>
            <input bind:value={curr.damage} type="number" class="input-form" name="damage" required/>

            <label for="image">Image:</label>
            <input bind:files type="file" class="input-form" name="image"/>

            <label for="sound">Sound:</label>
            <input bind:files={sounds} type="file" class="input-form" name="sound"/>

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
            <input bind:value={newEnemy.name} type="text" class="input-form" name="name" required/>

            <label for="xp">XP:</label>
            <input bind:value={newEnemy.xp} type="number" class="input-form" name="xp" required/>

            <label for="hp">HP:</label>
            <input bind:value={newEnemy.hp} type="number" class="input-form" name="hp" required/>

            <label for="mana">Mana:</label>
            <input bind:value={newEnemy.mana} type="number" class="input-form" name="mana" required/>

            <label for="damage">Damage:</label>
            <input bind:value={newEnemy.damage} type="number" class="input-form" name="damage" required/>

            <label for="image">Image:</label>
            <input bind:files type="file" class="input-form" name="image" required/>

            <label for="sound">Sound:</label>
            <input bind:files={sounds} type="file" class="input-form" name="sound"/>

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
        {#each enemies as enemy}
            <div class="enemy grid-item" on:click={() => curr = enemy}>
                <i class="material-icons" on:click={evt => deleteEnemy(evt, enemy.id)}>delete</i>
                <img src={enemy.image} alt="enemy" class="enemy-image" />
                <p class="label">Name</p>
                <p class="enemy-name">{enemy.name}</p>
                <p class="label">XP</p>
                <p class="enemy-health">{enemy.xp}</p>
                <p class="label">HP</p>
                <p class="enemy-health">{enemy.hp}</p>
                <p class="label">Mana</p>
                <p class="enemy-name">{enemy.mana}</p>
                <p class="label">Damage</p>
                <p class="enemy-name">{enemy.damage}</p>
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
</style>