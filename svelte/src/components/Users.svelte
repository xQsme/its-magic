<script lang="ts">
    import { DialogOverlay, DialogContent } from 'svelte-accessible-dialog';
    import axios from 'axios';
    import { url } from '../utils/server';
    import type { UserModel, GroupModel } from '../utils/models';

    let users:UserModel[] = [];
    let groups:GroupModel[] = [];
    let curr:UserModel = null;

    getUsers();
    getGroups();

    function getUsers() {
        axios.get(url + 'user/').then(result => {
            users = result.data;
            console.log(users);
        });
    }

    function getGroups() {
        axios.get(url + 'user/group/').then(result => {
            groups = result.data;
            console.log(groups);
        });
    }

    function handleEdit(evt) {
        evt.preventDefault();
        axios.put(url + 'user/' + curr.id + '/', curr).then(r => {
            curr=null;
            getUsers();
        }).catch(e => {
            alert('put error');
        });
    }

    function getUserRoles(user) {
        let roleNames = user.groups.map(group => {
            return group.name;
        })
        return roleNames.join(' | ');
    }
</script>

<DialogOverlay isOpen={curr !== null} onDismiss={() => curr = null}>
    <DialogContent class="dialog" aria-label="Announcement">
        <form class="dialog-container" on:submit={handleEdit}>
            <label for="first_name">Name:</label>
            <input bind:value={curr.first_name} type="text" class="input-form" name="first_name" required/>

            <label for="last_name">Surname:</label>
            <input bind:value={curr.last_name} type="text" class="input-form" name="last_name" required/>

            <label for="username">Username:</label>
            <input bind:value={curr.username} type="text" class="input-form" name="username" required/>

            <label for="email">Email:</label>
            <input bind:value={curr.email} type="text" class="input-form" name="email" required/>

            {#each groups as group}
                <div class="checkbox-group">
                    <input type="checkbox" name="{group.name}" checked={curr.groups.includes(group.id)} on:click={() => {
                        if(curr.groups.includes(group.id)) {
                            curr.groups.splice(curr.groups.indexOf(group.id), 1);
                        } else {
                            curr.groups.push(group.id);
                        }
                    }}/>
                    <label for="{group.name}">{group.name}</label>
                </div>
            {/each}

            <div class="dialog-buttons">
                <button>Submit</button>
                <button on:click={() => curr = null}>Close</button>
            </div>
        </form>
    </DialogContent>
</DialogOverlay>

<div class="users-container">
    <table>
        <thead>
            <tr>
                <th>Name</th>
                <th>Surname</th>
                <th>Username</th>
                <th>Email</th>
                <th>Roles</th>
                <th>Edit</th>
            </tr>
        </thead>
        <tbody>
            {#each users as user}
                <tr>
                    <td>{user.first_name}</td>
                    <td>{user.last_name}</td>
                    <td>{user.username}</td>
                    <td>{user.email}</td>
                    <td>{getUserRoles(user)}</td>
                    <td><i class="material-icons" on:click={() => {
                        curr = user;
                        curr.groups = curr.groups.map(group => {
                            return group.id;
                        });
                    }}>edit</i></td>
                </tr>
            {/each}

        </tbody>
    </table>
</div>

<style lang="scss">

    .users-container{
        width: 100%;
        overflow: auto;
        display: flex;

        .material-icons{
            cursor: pointer;
        }

        .material-icons:hover{
            color: orangered;
        }
    }

    .checkbox-group{
        display: flex;

        input{
            margin-right: 10px;
        }
    }

    table {
        width: calc(100% - 40px);
        margin: 20px;
    }

    thead {
        display:flex;
        width:100%;
    }


    tr {
        display:flex;
        width:100%;
    }

    tbody{
        tr:nth-child(odd) {
            background:#303030;
        }
    }




    td, th {
        flex: 1 1 20%;
        text-align:center;
        border: 1px solid darkgray;
        padding: 5px;
    }

    th{
        padding: 20px;
    }


</style>