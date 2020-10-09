<script lang="ts">
    export let enemy:Enemy;
</script>

<div class="container">
    <div class="container2">
        <img src="./assets/images/health.png">
        <div class="centered" style="color: red">{enemy.hp}/{enemy.hp}</div>
    </div>
    <div class="container2">
        <img src="./assets/images/mana.png">
        <div class="centered" style="color: cornflowerblue">{enemy.time}/{enemy.time}</div>
    </div>
    
    <img class="enemy" src={enemy.image} alt="enemy"/>   
</div>
     
<style lang="scss">
    .container{
        display: flex;
        background-color: #303030;
        flex-direction: column;
        flex: 1 1 auto;

        .container2 {
            position: relative;
            text-align: center;
            
            .centered {
                position: absolute;
                top: 72.5%;
                left: 62.5%;
                transform: translate(-50%, -50%);
                font-size: 64px;
                border: 5px solid #555; 
            }

        }
        .enemy{        
            border: 5px solid #555; 
            flex: 1;
        }
    }


    

</style>