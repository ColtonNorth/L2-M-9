package com.example.thequalityflow;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;

import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;
import androidx.navigation.fragment.NavHostFragment;

public class SecondFragment extends Fragment {
    @Override
    public View onCreateView(
            LayoutInflater inflater, ViewGroup container,
            Bundle savedInstanceState
    ) {
        View myView =inflater.inflate(R.layout.fragment_second, container, false);
        WebView myWebView1 = myView.findViewById(R.id.WebView1);
        WebView myWebView2 = myView.findViewById(R.id.WebView2);
        WebView myWebView3 = myView.findViewById(R.id.WebView3);
        WebView myWebView4 = myView.findViewById(R.id.WebView4);
        WebView myWebView5 = myView.findViewById(R.id.WebView5);
        WebView myWebView6 = myView.findViewById(R.id.WebView6);
        myWebView1.setWebViewClient(new WebViewClient());
        myWebView2.setWebViewClient(new WebViewClient());
        myWebView3.setWebViewClient(new WebViewClient());
        myWebView4.setWebViewClient(new WebViewClient());
        myWebView5.setWebViewClient(new WebViewClient());
        myWebView6.setWebViewClient(new WebViewClient());
        myWebView1.loadUrl("https://thingspeak.com/channels/1226418/charts/1?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&type=line&update=15");
        myWebView2.loadUrl("https://thingspeak.com/channels/1226418/charts/2?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&type=line&update=15");
        myWebView3.loadUrl("https://thingspeak.com/channels/1226418/charts/3?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&type=line&update=15");
        myWebView4.loadUrl("https://thingspeak.com/channels/1226517/charts/1?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&type=line&update=15");
        myWebView5.loadUrl("https://thingspeak.com/channels/1226517/charts/2?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&type=line&update=15");
        myWebView6.loadUrl("https://thingspeak.com/channels/1226517/charts/3?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&type=line&update=15");
        WebSettings webSettings = myWebView1.getSettings();
        webSettings.setJavaScriptEnabled(true);
        WebSettings webSettings2 = myWebView2.getSettings();
        webSettings2.setJavaScriptEnabled(true);
        WebSettings webSettings3 = myWebView3.getSettings();
        webSettings3.setJavaScriptEnabled(true);
        WebSettings webSettings4 = myWebView4.getSettings();
        webSettings4.setJavaScriptEnabled(true);
        WebSettings webSettings5 = myWebView5.getSettings();
        webSettings5.setJavaScriptEnabled(true);
        WebSettings webSettings6 = myWebView6.getSettings();
        webSettings6.setJavaScriptEnabled(true);


        // Inflate the layout for this fragment
        return myView;
    }

    public void onViewCreated(@NonNull View view, Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);

        view.findViewById(R.id.button_second).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                NavHostFragment.findNavController(SecondFragment.this)
                        .navigate(R.id.action_SecondFragment_to_FirstFragment);
            }
        });
    }
}