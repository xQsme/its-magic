<div class="register-page">
    <div class="form">
        <h1>Register</h1>
      <form class="register-form">
        <input type="text" placeholder="First Name" class="input-form" name="firstname" id="firstname"/>
        <input type="text" placeholder="Last Name" class="input-form" name="lastname" id="lastname"/>
        <input type="text" placeholder="Username" class="input-form" name="username" id="username"/>
        <input type="email" placeholder="Email Address" class="input-form" />
        <input type="password" placeholder="Password" class="input-form" name="password" id="password"/>
        <button type="submit" class="formSubmit">create</button>
      </form>
    </div>
  </div>
<style lang="scss">
    .input-form{
        display: block;
        text-align: center;
        margin-top: 1.5em;
        margin-bottom: 1.5em;
    }
    .register-page{
        text-align: center;
        margin-left: auto;
        margin-right: auto;
    }
    .formSubmit{
        text-decoration: none;
        background-color: #28a745;
        border-color: #28a745;
        color: #fff;
        text-align: center;
        border-radius: .5em;
    }

</style>