import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:lottie/lottie.dart';
import 'package:thesecurityman/onboarding.dart';

class SplashScreen extends StatefulWidget {
  SplashScreen({Key key}) : super(key: key);

  @override
  _SplashScreenState createState() => _SplashScreenState();
}


  @override
  Widget build(BuildContext context) {
    //Safearea is
    return SafeArea(child: Scaffold(
      backgroundColor: Colors.white,
      body: Fixed(
          alignment: Alignment.center,
          child: Column(
              crossAxisAlignment: CrossAxisAlignment.center,
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[
                FixedButton(
                    height: 350,
                    width: 350,
                    child: Lottie.asset("assets/tsm.json")),
                SizedBox(height: 20),
                Text("The Security Man",
                    style: TextStyle(
                        color: mainColor,
                        fontWeight: FontWeight.bold,
                        fontFamily: 'Hina')),
                SizedBox(
                  height: 150,
                ),
                TextButton(
                  "All Rights Are Reserved, Since @ 2021",
                  style: TextStyle(fontSize: 20, fontFamily: 'Hina'),
                )
              ])),
    ));
  }
}
