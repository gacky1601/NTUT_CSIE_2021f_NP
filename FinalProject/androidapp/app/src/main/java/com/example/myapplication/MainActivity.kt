package com.example.myapplication

import android.graphics.Color
import android.os.Build
import android.os.Bundle
import android.text.format.DateFormat
import android.view.View
import android.widget.AdapterView
import androidx.annotation.RequiresApi
import androidx.appcompat.app.AppCompatActivity
import com.google.firebase.firestore.FirebaseFirestore
import kotlinx.android.synthetic.main.activity_main.*
import org.jetbrains.anko.toast
import java.text.SimpleDateFormat
import java.time.Instant
import java.time.LocalDateTime
import java.util.*


class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        //變數宣告
        var twrate_local:Double = 4.256
        var paybaorate_local:Double = 4.275
        //firebase
        var db = FirebaseFirestore.getInstance()
        var dbpath=db.collection("exchange_rate")
        var checkdate=dbpath.document("last_update")
        var current_type:String="USD"

        spinner.onItemSelectedListener = object :
            AdapterView.OnItemSelectedListener {
            override fun onItemSelected(
                parent: AdapterView<*>?,
                view: View?,
                position: Int,
                id: Long
            ) {
                current_type=spinner.selectedItem.toString()
                checkdate.get()
                    .addOnSuccessListener { document ->
                        var db_timestamp= document.getString("timestamp").toString().toLong()
                        serverdate_tv.text=SimpleDateFormat("yyyy-MM-dd ahh:mm").format(db_timestamp*1000)
                        var getexchangerate=dbpath.document(db_timestamp.toString())
                        getexchangerate.get()
                            .addOnSuccessListener { document ->

                                twrate_local= document.getDouble(current_type)!!
                                twexc_tv.text=twrate_local.toString()
//                                paybaorate_local=document.getDouble("USD")!!
//                                paybaoexc_tv.text=current_type
                            }
                            .addOnFailureListener { exception ->
                                twexc_tv.text="error"
//                                paybaoexc_tv.text="error"
                            }
                        inputnum.hint= "Convert $current_type to NTD"
                    }
                    .addOnFailureListener { exception -> toast("請連接網路") }
            }

            override fun onNothingSelected(parent: AdapterView<*>?) {
                TODO("Not yet implemented")
            }


        }

        //轉換
        calculate_button.setOnClickListener {
            try{
                val mynum: Int = inputnum.text.toString().toInt()
                twresult_tv.text = ((((mynum * twrate_local)*100).toInt().toFloat())/100).toString()
//                paybaoresult_tv.text = ((((mynum * paybaorate_local)*100).toInt().toFloat())/100).toString()
//                var result=(((((mynum * twrate_local) - (mynum * paybaorate_local))*100).toInt()).toFloat())/100
//                diff_tv.text = (result.toString())
            }
            catch(e: Exception){
                toast("請輸入有效值")
            }
//            if(twrate_local<paybaorate_local){twresult_tv.setBackgroundColor(Color.parseColor("#66BB6A"))}
//            else{paybaoresult_tv.setBackgroundColor(Color.parseColor("#66BB6A"))}
        }
    }
}




